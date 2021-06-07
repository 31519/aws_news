from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Number, Again
from django.shortcuts import get_object_or_404
# Create your views here.
def form(request):
    user=request.user
    number = get_object_or_404(Again, user=user)
    # number = Again.objects.all()
    context = {
        'number':number,
        'user':user
    }
    return render(request, 'ajax/form.html', context)

def again(request):
    num = get_object_or_404(Again, user=request.user)
    
    # product = num.number.all()
    cart_data = {'number':num.number, 'name':num.name}
    return JsonResponse(cart_data)
    
def getProfiles(request):
    profiles = Again.objects.all()
    # print(profiles.name)
    # return JsonResponse(profiles)
    return JsonResponse({"profiles":list(profiles.values())})

def ajax_view(request, num_id):
    if request.is_ajax():
        print("ajax request")
    print(num_id)
    num = get_object_or_404(Again, id=num_id)
    num.number += 1 
    num.save()
    return HttpResponse("succeed")


def create(request):
    if request.method == 'POST':
        # new_profile = Again()
        new_profile = get_object_or_404(Again, user=request.user)
        new_profile.number += 1  
        new_profile.save()
        add = "hi"
        if request.is_ajax():
            print("Ajax request")
            json_data = {
                "add":add,
                "num":new_profile.number
            }
            return JsonResponse(json_data)
        return HttpResponse("New profile creates successfully")






