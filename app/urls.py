from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage, name='home'),
    path('doctors/', views.Doctor, name='doctors'),
    path('departments/', views.Department, name='departments'),
    path('department/<int:pk>/', views.Departments_details, name='department_detail'),
    path('booking/', views.Booking, name='booking'),
    path('create/', views.Create_dpt, name='create'),
    path('login/', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('feedback/', views.Feedbacklist , name='feedback'),
]