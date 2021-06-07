
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form, name="form"),
    path('getProfiles', views.getProfiles, name="getProfiles"),
    path('create/', views.create, name="create"),
    path('again/', views.again, name="again"),
    path('ajax_view/<int:num_id>/', views.ajax_view, name="ajax_view")


]
