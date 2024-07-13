from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage,name='home'),
    path('doctors/', views.Doctor,name='doctors'),
    path('departments/', views.Department,name='departments'),
    path('booking/', views.Booking,name='booking'),
    path('create/',views.Create_dpt,name='create'),
]