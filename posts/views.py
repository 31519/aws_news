from django.db import reset_queries
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Posts
from newsapi import NewsApiClient
import requests
import json
from advertise.models import Ads_Payment, Advertise
from .forms import PostsForms
from django.contrib.auth.decorators import login_required
from about_us.models import AboutUs
from django.contrib import messages


news_api = "d049a308e4634c8b8a28ce3b4b3059be"
# Create your views here.
def home(request):
    return render(request, 'home.html')



def local_news(request):
    ads = Ads_Payment.objects.filter(active="True")
    posts = Posts.objects.all()

    context = {
        'ads': ads,
        'posts':posts
    }
    return render(request, 'post/local_news.html', context)

def business(request):
    ads = Ads_Payment.objects.filter(active="True")
    category = request.GET.get('category')

    
  
    url = f'https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={news_api}'
    # url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}'
    response = requests.get(url)
    data = response.json()
    article = data['articles']

    # Headline
    newsapi = NewsApiClient(api_key=news_api)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                            category='business',
                                            language='en',
                                            country='us')
    top_headline = top_headlines['articles']                         
            

    
    context = {
        'article': article,
        'top_headline':top_headline,
        'ads':ads
    }
        
    
    return render(request, 'post/business.html', context)

def post_detail(request, category_slug, post_slug):
    try:
        posts = Posts.objects.get(category__slug=category_slug, slug=post_slug)
    except Exception as e:
        raise e
    context = {
        'posts': posts
    }
    return render(request, 'post/post_detail.html', context)


@login_required(login_url='login')
def publish(request):
    post = Posts.objects.all()
    if request.method == 'POST':
        form = PostsForms(request.POST, request.FILES)
        if form.is_valid():
            post = Posts()
            post.category = form.cleaned_data['category']
            post.description = form.cleaned_data['description']
            post.heading = form.cleaned_data['heading']
            post.images = form.cleaned_data['images']
            post.post_name = form.cleaned_data['post_name']
            post.published_date = form.cleaned_data['published_date']

            post.save()
            messages.success(request, "Successfully Upload Your Post")
            return redirect('publish')
        else:
            messages.error(request, "Failed to Upload Your Post")
            return redirect('publish')
    else:
        form = PostsForms()

    context = {
        'form':form,
        'post':post
    }
    
    return render(request, 'post/publish.html', context)

@login_required(login_url='login')
def edit_publish(request, p_id):
    post = get_object_or_404(Posts, id=p_id)
    if request.method == 'POST':
        form = PostsForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited your Post")
            return redirect('publish')
        else:
            messages.error(request, "Failed to Edited your Post")
            return redirect('publish')
    else:
        form = PostsForms(instance=post)
    context = {
        'form':form,
        'post':post
    }
    
    return render(request, 'post/edit_publish.html', context)


@login_required(login_url='login')
def delete_publish(request, p_id):
    post = get_object_or_404(Posts, id=p_id)
    post.delete()
    messages.success(request, "Successfully Deleted Your Post")

    return redirect('publish')




def about_us(request):
    aboutus= AboutUs.objects.all()


    context = {
        'about':aboutus
    }
    return render(request, 'post/about_us.html', context)