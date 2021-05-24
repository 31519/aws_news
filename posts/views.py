from django.shortcuts import render
from .models import Posts
from marketing.models import Signup
from marketing.forms import SignupForm

# Create your views here.
def home(request):
    return render(request, 'home.html')



def local_news(request):
    posts = Posts.objects.all()
    form = SignupForm()
    context = {
        'posts': posts,
        'form':form
    }
    return render(request, 'post/local_news.html', context)


def post_detail(request, category_slug, post_slug):
    try:
        posts = Posts.objects.get(category__slug=category_slug, slug=post_slug)
    except Exception as e:
        raise e
    context = {
        'posts': posts
    }
    return render(request, 'post/post_detail.html', context)