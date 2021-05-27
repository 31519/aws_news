from django.db import reset_queries
from django.shortcuts import render
from .models import Posts
from marketing.models import Signup
from marketing.forms import SignupForm
from newsapi import NewsApiClient
import requests
import json

news_api = "d049a308e4634c8b8a28ce3b4b3059be"
# Create your views here.
def home(request):
    return render(request, 'home.html')



def local_news(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}'
    response = requests.get(url)
    data = response.json()
    article = data['articles']
    context = {
        'article': article,
    }
    return render(request, 'post/local_news.html', context)

def business(request):

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
        'top_headline':top_headline
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