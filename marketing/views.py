from django import forms
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import SignupForm
from .models import Signup
from django.http import HttpResponse
# Create your views here.
import requests
import json
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect




MAILCHIMP_API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', None)
MAILCHIMP_DATA_CENTER = getattr(settings, 'MAILCHIMP_DATA_CENTER', None)
MAIL_CHIMP_EMAIL_LIST_ID =getattr(settings, 'MAIL_CHIMP_EMAIL_LIST_ID', None)


api_url = f"https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0"
members_endpoint = f'{api_url}/lists/{MAIL_CHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
            
        
        data= {
            'email_address':email,
            'status':'subscribed'
        }
        
        r = requests.post(members_endpoint, auth=("", MAILCHIMP_API_KEY), data=json.dumps(data))
        return HttpResponse("hi form json")

def email_list_signup(request):
    form = SignupForm(request.POST , None)

    if request.method == 'POST':
        if form.is_valid():
            email = request.POST['email']
            signup_qs = Signup.objects.filter(email=email)
            data = Signup()
            
            if signup_qs.exists():
                messages.success(request, 'Already subscribe')
            else:
                subscribe(email)
                form.save()
                messages.success(request, 'successfully subscribe')
                return HttpResponse("hi")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

