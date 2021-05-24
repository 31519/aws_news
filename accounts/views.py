from decimal import Context
from django.http.response import HttpResponse
from accounts.models import Account, UserProfile
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
# VERIFICATIONS EMAILS
from django.contrib.sites.shortcuts import get_current_site# Create your views here.
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage, send_mail


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
            
            subject = ("Please Activate your Account")
            message = render_to_string('email/activate.html', {
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

            })
            to_email = email
            send_mail = EmailMessage(subject, message, to=[to_email])
            send_mail.send()
            # send_mail(subject, message, to_email)
            
            user.save()
            profile = UserProfile()
            profile.user_id = user.id
            profile.images = 'default/default-user.jpg'
            profile.save()

            messages.success (request, f"your account {user.username} has been create successfully")


            return redirect('login')
        else:
            return HttpResponse("hi")

            
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

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request, 'Registering successful')
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
            return redirect('account/forgot_password.html')
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

        messages.success(request, "Reset Your password")
        return redirect('reset_my_password')

    else:
        return HttpResponse("hi")
        exit()
        return redirect('login')

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
    profile = get_object_or_404(UserProfile, user=user)
    adv = Advertise.objects.all().filter(user=user)
    user_profile = UserProfile.objects.all().filter(user=user)
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
            return redirect('dashboard')
        else:
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
        profile_form = UserProfileForm(request.POST, instance=user_profile)
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
                messages.error(request, 'Invalic Current Password!')
                return redirect('change_password')
        else:
            messages.error(request, 'Password Change Not Complete')
            return redirect('change_password')
    return render(request, 'account/change_password.html')







