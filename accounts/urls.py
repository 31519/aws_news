from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('reset_my_password/', views.reset_my_password, name='reset_my_password'),
    path('reset_password_email/<uidb64>/<token>/', views.reset_password_email, name='reset_password_email'),
    path('change_profile/', views.change_profile, name='change_profile')
]