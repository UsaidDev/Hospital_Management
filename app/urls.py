from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage,name='home'),
    path('about/', views.About,name='about'),
    path('services/', views.Services,name='services'),
    path('contact/', views.Contact,name='contact'),
]