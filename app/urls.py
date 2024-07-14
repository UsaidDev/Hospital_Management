from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage,name='home'),
    path('doctors/', views.Doctor,name='doctors'),
    path('departments/', views.Department,name='departments'),
    path('booking/', views.Booking,name='booking'),
    path('create/',views.Create_dpt,name='create'),
    path('signup/',views.Signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout')
]