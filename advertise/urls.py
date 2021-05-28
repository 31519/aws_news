from django.urls import path, include
from . import views

urlpatterns = [
    path('upload_advertise/', views.upload_advertise, name='upload_advertise'),
    path('advertise_detail/<slug:category_slug>/<slug:advertise_slug>/', views.advertise_detail, name='advertise_detail'),
    path('edit_advertise/<int:my_id>/', views.edit_advertise, name='edit_advertise'),
    path('delete_advertise/<int:my_id>/', views.delete_advertise, name='delete_advertise'),

]
