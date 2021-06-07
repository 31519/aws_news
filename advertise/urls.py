from django.urls import path, include
from . import views

urlpatterns = [
    path('upload_advertise/', views.upload_advertise, name='upload_advertise'),
    path('upload_advertise_checkout/', views.upload_advertise_checkout, name='upload_advertise_checkout'),
    path('view_advertise/', views.view_advertise, name='view_advertise'),
    path('advertise_detail/<slug:category_slug>/<slug:advertise_slug>/', views.advertise_detail, name='advertise_detail'),
    path('edit_advertise/<int:my_id>/', views.edit_advertise, name='edit_advertise'),
    path('delete_advertise/<int:my_id>/', views.delete_advertise, name='delete_advertise'),
    path('refresh', views.refresh, name='refresh'),
    path('advertise_view/<int:my_id>/', views.advertise_view, name='advertise_view'),
    path('success/', views.success, name='success'),

]
