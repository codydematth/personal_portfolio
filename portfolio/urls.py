from django.urls import path
from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.homeView, name='index'),
    path('posts/', views.postsView, name= 'posts'),
    path('post/<slug:slug>/', views.postView, name= 'post'),

    #send Email
    path('send_email/', views.sendEmail, name="send_email"),

    #Favicon
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('my_portfolio/img/favicon.ico')))
]