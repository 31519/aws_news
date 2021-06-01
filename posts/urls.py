from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.local_news, name='local_news'),
    path('publish/', views.publish, name='publish'),
    path('business/', views.business, name='business'),
    path('post_detail/<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),

    # email
    path('edit_publish/<int:p_id>/', views.edit_publish, name='edit_publish'),
    path('delete_publish/<int:p_id>/', views.delete_publish, name='delete_publish'),
    path('about_us/', views.about_us, name='about_us'),

]
