from django import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import AdvertiseForm
from .models import Ads_Payment, Advertise
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@login_required(login_url='login')
def upload_advertise(request):
    my_ads = Advertise.objects.filter(user=request.user).order_by('-adv_created_date')
    if request.method == "POST":
        form = AdvertiseForm(request.POST, request.FILES)
        if form.is_valid():
            advertises = Advertise()
            advertises.user = request.user
            advertises.adv_heading = form.cleaned_data['adv_heading']
            advertises.adv_descriptions = form.cleaned_data['adv_descriptions']
            advertises.adv_start_date = form.cleaned_data['adv_start_date']
            advertises.adv_end_date = form.cleaned_data['adv_end_date']
            advertises.adv_category = form.cleaned_data['adv_category']
            advertises.adv_images = form.cleaned_data['adv_images']
            print("adv")
            advertises.adv_plan = request.POST['adv_plan']
            print("adv2")
            data = datetime.now()
            year = data.year
            month = data.month
            day = data.day
            hours = data.hour
            minute = data.minute
            second = data.second
            times =int(f"{year}{month}{day}{hours}{minute}{second}")
            order_number = times
            advertises.adv_order_number = order_number

            advertises.save()

            
            messages.success(request, "Successfully Uploaded Your Advertise")
            return redirect('upload_advertise_checkout')
            # return render(request, 'advertise/upload_advertise_checkout.html', context)
        else:
            messages.error(request, "Failed to upload your advertise")
            return redirect('upload_advertise')
    else:
        form = AdvertiseForm()

    context = {
        'form':form,
        'my_ads':my_ads
    }
    return render(request, 'advertise/my_advertise.html', context)

def upload_advertise_checkout(request):
    ads = Advertise.objects.filter(user=request.user).order_by('-adv_datetime_now')[0]
    
    if request.method == "POST":
        # form = AdsPaymentForm(request.POST)
        # if form.is_valid():
        payments = Ads_Payment()

        payments.user = request.user
        payments.advertise = ads
        print('adv_plan')
        payments.adv_plan = ads.adv_plan
        payments.order_number = ads.adv_order_number
        # payments.active = "True"
        payments.save()
        print('payment.save')
        amount = ads.adv_plan
        client = razorpay.Client(auth=("rzp_test_04krTrtQkeKgfM", "hyO1Hm9hglRKqOrj3znsxLxL"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        payments.active = "True"
        
        email  = ads.user.email
        print(email)

        user = request.user
        print(user)
        subjects = "Your subscribtion has been activate! "
        to_email = [email,]
        message = render_to_string('email/ads_email.html', {
            'user':user,
        })
        print("activate email4")
        send_mail = EmailMessage(subjects, message, to=to_email)
        print("activate email5")
        send_mail.send()
        print("finished activate email")
        messages.success(request, "successfully upload your ads")
        return redirect('upload_advertise')
    else:
        context  = {
            'ads':ads,
        }
        return render(request, 'advertise/upload_advertise_checkout.html', context)

@csrf_exempt
def success(request):
    return render(request, 'success.html')


@login_required(login_url='login')
def advertise_detail(request, category_slug, advertise_slug):
    try:
        adv = Advertise.objects.get(adv_category__slug=category_slug, slug=advertise_slug)
    except Exception as e:
        raise e
    context = {
        'adv':adv
    }
    return render(request, 'advertise/my_advertise_detail.html', context)

@login_required(login_url='login')
def edit_advertise(request, my_id):

    ads = get_object_or_404(Advertise, id=my_id)
    print(ads.id)

    if request.method == "POST":
        form = AdvertiseForm(request.POST, request.FILES, instance=ads)
        if form.is_valid():
            # advertises = Advertise()
            form.save()
            messages.success(request, "Successfully Edited Your Adv")
            return redirect('upload_advertise')
        else:
            messages.error(request, "Failed To Edit Your Ads")
            return redirect('upload_advertise')
            # return redirect('advertise')
    else:
        form = AdvertiseForm(instance=ads)

    context = {
        'form':form,
        'ads':ads
    }
        
    return render(request, 'advertise/edit_advertise.html', context)


@login_required(login_url='login')
def delete_advertise(request, my_id):
    ads = get_object_or_404(Advertise, id=my_id)
    ads.delete()
    # ads.save()
    messages.success(request, 'Successfully Deleted Your Ads')
    return redirect('upload_advertise')


def view_advertise(request):
    ads = Ads_Payment.objects.filter(active='True')
    # ads = Advertise.objects.filter(adv_display="True")
    context = {
        'ads':ads
    }
    return render(request, 'advertise/view_advertise.html', context)




# detail ads from the local news
def advertise_view(request, my_id):
    adv = get_object_or_404(Advertise, id=my_id)
    context = {
        'adv':adv
    }
    return render(request, 'advertise/advertise_view.html', context)


def refresh(request):
    # adv = Advertise()
    # from datetime import datetime, timedelta
    # for loop in adv.adv_datetime_now:
    #     now = adv.adv_datetime_now
    #     data = now + timedelta(days=1)
    #     if (datetime.now()) >= data:
    #         adv.adv_display = "False"
    #         print("False")
    #         adv.save()
    #     else:
    #         adv.adv_display = "True"
    return redirect('view_advertise')