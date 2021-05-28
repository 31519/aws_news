from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import AdvertiseForm
from .models import Advertise
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def upload_advertise(request):
    my_ads = Advertise.objects.filter(user=request.user)
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
            advertises.save()
            return redirect('upload_advertise')
        else:
            return redirect('advertise')
    else:
        form = AdvertiseForm()

    context = {
        'form':form,
        'my_ads':my_ads
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

@login_required(login_url='login')
def edit_advertise(request, my_id):

    ads = get_object_or_404(Advertise, id=my_id)
    print(ads.id)

    if request.method == "POST":
        form = AdvertiseForm(request.POST, request.FILES, instance=ads)
        if form.is_valid():
            # advertises = Advertise()
            form.save()
            return redirect('upload_advertise')
        else:
            return HttpResponse('upload_advertise')
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
    return redirect('upload_advertise')