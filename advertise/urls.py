from django.urls import path, include
from . import views

urlpatterns = [
    path('advertise/', views.advertise, name='advertise'),
    path('advertise_detail/<slug:category_slug>/<slug:advertise_slug>/', views.advertise_detail, name='advertise_detail'),

]
