from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Departments
from . models import Doctors
from .form import BookingForm
from . models import Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def MainPage(request):
    user = request.user
    departments = Departments.objects.all()

    return render(request, 'index.html', {'user': user, 'departments': departments})

def Doctor(request):
    doctors=Doctors.objects.all()
    return render(request, 'doctors.html',{'doctors': doctors})

def Department(request):
    departments=Departments.objects.all()
    return render(request, 'departments.html',{'departments':departments})

def Create_dpt(request):
    if request.method == 'POST':
        dep_name=request.POST.get('dep_name')
        dep_description=request.POST.get('dep_description')
        Departments.objects.create(dep_name=dep_name,dep_description=dep_description)
        return redirect('home')
    return render(request, 'create.html')

def Booking(request):
    error_meg=None
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conformation.html')
        else:
            error_meg='Check datas'
    else:
        form=BookingForm()
    dic_frm={
        'form':form,
        'error_message':error_meg
    }
    return render(request, 'booking.html',dic_frm)

def Signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Username already existed')
            return redirect('signup')
        
        user=User.objects.create_user(username=username,
        email=email)

        user.set_password(password)
        user.save()
        messages.success(request, 'Account Created successfully')
        return redirect('login')
    return render(request , 'signup.html')

def Login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not username:
            messages.error(request,"Username field is required")
            return redirect('login')
        if not password:
            messages.error(request,"Password field is required")
            return redirect('login')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return render('login')

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')
    return render(request , 'login.html')

def Logout(request):
    logout(request)
    return redirect('home')