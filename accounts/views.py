# from decimal import Context
# from django.db.models.fields import EmailField
# from django.http.response import HttpResponse
from accounts.models import Account, UserProfile, WriteToUs
from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm, UserProfileForm, UserForm
from .models import Account, UserProfile
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from advertise.models import Advertise
from datetime import datetime
from django.contrib import messages
from django.forms import modelformset_factory

# VERIFICATIONS EMAILS
from django.contrib.sites.shortcuts import get_current_site# Create your views here.
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("2")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            country = form.cleaned_data["country"]
            state = form.cleaned_data["state"]
            gender = form.cleaned_data["gender"]
            username = email.split('@')[0]
            password = form.cleaned_data["password"]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            user.country = country
            user.phone_number = phone_number
            user.state = state
            user.gender = gender
            
            
            current_site  = get_current_site(request)
            print("activate email1")
            subject = ("Please Activate your Account")
            print("activate email2")
            message = render_to_string('email/activate.html', {
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),

            })
            print("activate email3")
            
                # 'token':default_token_generator.make_token(user),
            to_email =[email,]
            print("activate email4")
            # from_email = settings.EMAIL_HOST_USER
            send_mail = EmailMessage(subject, message, to=to_email)
            # send_mail(subject, message, from_email,  to_email   )
            print("activate email5")
            # send_mail.send()
            send_mail.send()
            print("finished activate email")
            # send_mail(subject, message, to_email)
            
            user.save()
            profile = UserProfile()
            profile.user_id = user.id
            profile.images = 'default/default-user.jpg'
            profile.save()

            messages.success(request, "Your Account has been create successfully")
            return redirect('login')
        else:
            messages.error(request, "Invalid credential!")
            return redirect('register')

            
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'account/register.html', context)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user  = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user=None

    if user is not None:
        # and default_token_generator.check_token(user,token)
        user.is_active = True
        user.save()
        messages.success(request, 'Your Account has been create successfully')
        return redirect('login')
    else:
        messages.error('Error in registering')
        return redirect('register')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists:
            user = Account.objects.get(email__exact=email)
            current_site = get_current_site(request)
            subject = "Please Reset Your Password !"

            message = render_to_string('email/forgotPassword.html', {
                'user':user,
                'domain':current_site,
                'token':default_token_generator.make_token(user),
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            })
            to_mail = email
            send_mail = EmailMessage(subject, message, to=[to_mail])
            send_mail.send()
            messages.success(request, "Reset Password email has been send to this email")
            return redirect('forgot_password')
        

        else:
            messages.error(request, "We could not find your email! ")
            return redirect('forgot_password')
    return render(request, 'account/forgot_password.html')

def reset_password_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user  = Account._default_manager.get(pk=uid)
        print("try")

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        print("exception")
        user = None
    print("try and excepy")
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        return redirect('reset_my_password')

    else:
        messages.error(request, "Invalid token! ")
        return redirect('forgot_password')
        

def reset_my_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session['uid']
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Your Password Has Been Change')
            return redirect('login')
        else:
            messages.error(request, 'Reset Not SuccessFull')
            return redirect('reset_my_password')
    return render(request, 'account/reset_my_password.html')

def change_profile(request):
    return render(request, 'account/change_profile.html')
    

@login_required(login_url='login')
def dashboard(request):
    today = datetime.now()
    user =  request.user
    
    # profile = get_object_or_404(UserProfile, user=user)
    adv = Advertise.objects.all().filter(user=user)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    print(user_profile)
    # return HttpResponse(user_profile.images)
    context = {
        'adv':adv,
        'date':today,
        'profile':user_profile
    }
    return render(request, 'account/dashboard.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:

            auth.login(request, user)
            messages.success(request, "Successfully Loged in")
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid credential !")
            return redirect('login')
    return render(request, 'account/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def change_profile(request):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    user = request.user
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        user_form = UserForm(request.POST, instance=user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "Your Profile has been change successfully")
            return redirect('dashboard')
        else:
            messages.error(request, 'Profile not Update')
            return redirect('change_profile')
    else:
        profile_form = UserProfileForm(instance=user_profile)
        user_form = UserForm(instance=user)

    context = {
        'profile':user_profile,
        'profileForm':profile_form,
        'userForm':user_form
    }
    return render(request, 'account/change_profile.html', context)
            


@login_required(login_url='login')
def change_password(request):


    if request.method == 'POST':
        current = request.POST['current_password']
        new  = request.POST['new_password']
        confirm  = request.POST['confirm_new_password']
        user = Account.objects.get(username__exact=request.user.username)
        if new == confirm:
            success = user.check_password(current)
            if success:
                user.set_password(new)
                user.save()
                messages.success(request, 'Password Change Successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Could not find your current password !')
                return redirect('change_password')
        else:
            messages.error(request, 'New and confirm password must be the same!')
            return redirect('change_password')

        
    return render(request, 'account/change_password.html')



def write_to_us(request):
    user =  request.user
    if request.method == 'POST':
        email = request.POST['email']
        text = request.POST['text']
        data = WriteToUs()
        data.email = email
        data.text = text
        user_name = email.split('@')[0]
        print(user_name)
        data.save()

        # Sending email to them
        subject = 'Thank you for writing to us'
        to_email = [email,]
        message = render_to_string('email/write_to_us.html', {
            'user_name':user_name
        })
        # from_email = settings.EMAIL_HOST_USER
        from_email = 'markospale31519@gmial.com'
        # send_mail = EmailMessage(subject, message, to=[to_email])
        send_mail(subject, message, from_email, to_email)
        messages.success(request, "Thank You, Hope you have a nice day")
        return redirect('write_to_us')

    else:
        # messages.error(request, "Sorry, There is an error")
        return render(request, 'account/write_to_us.html')

    # return render(request, 'account/write_to_us.html')







