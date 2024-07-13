from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage,name='home'),
    path('about/', views.About,name='about'),
    path('departments/', views.Department,name='departments'),
    path('contact/', views.Contact,name='contact'),
    path('create/',views.Create_dpt,name='create'),
]