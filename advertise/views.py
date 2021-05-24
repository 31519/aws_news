from django.shortcuts import redirect, render
from .forms import AdvertiseForm
from .models import Advertise
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def advertise(request):
    if request.method == "POST":
        form = AdvertiseForm(request.POST)
        if form.is_valid():
            advertises = Advertise()
            advertises.user = request.user
            advertises.adv_heading = form.cleaned_data['adv_heading']
            advertises.adv_descriptions = form.cleaned_data['adv_descriptions']
            advertises.adv_conclude = form.cleaned_data['adv_conclude']
            advertises.adv_start_date = form.cleaned_data['adv_start_date']
            advertises.adv_end_date = form.cleaned_data['adv_end_date']
            advertises.adv_category = form.cleaned_data['adv_category']
            advertises.adv_images = form.cleaned_data['adv_images']
            advertises.save()
        else:
            return redirect('advertise')
    else:
        form = AdvertiseForm()

    context = {
        'form':form
    }
    return render(request, 'advertise/my_advertise.html', context)


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
