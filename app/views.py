from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Departments, Doctors, Feedback, Booking
from .form import BookingForm
from django.contrib.auth.decorators import login_required

# Main Page View
@login_required(login_url='login')
def MainPage(request):
    user = request.user
    departments = Departments.objects.all()
    return render(request, 'index.html', {'user': user, 'departments': departments})

# Doctor List View
def Doctor(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

# Department List View
def Department(request):
    departments = Departments.objects.all()
    return render(request, 'departments.html', {'departments': departments})

# Department Details View
def Departments_details(request, pk):
    department = get_object_or_404(Departments, pk=pk)
    return render(request, 'departments.html', {'department': department})

# Create Department View
def Create_dpt(request):
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_description = request.POST.get('dep_description')
        Departments.objects.create(dep_name=dep_name, dep_description=dep_description)
        return redirect('home')
    return render(request, 'create.html')

# Booking View
def Booking(request):
    error_meg = None
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conformation.html')
        else:
            error_meg = 'Check the data'
    else:
        form = BookingForm()
    dic_frm = {
        'form': form,
        'error_message': error_meg
    }
    return render(request, 'booking.html', dic_frm)

# Signup View
def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number=request.POST.get("phone")
        Address = request.Post.get("Address")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Account Created Successfully!!')
        return redirect('login')
    return render(request, 'signup.html')

# Login View
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Validation checks
        if not username:
            messages.error(request, "Username field is required")
            return redirect('login')
        if not password:
            messages.error(request, "Password field is required")
            return redirect('login')
        # Check if username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('login')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')
# Logout View

def Logout(request):
    logout(request)
    return redirect('home')

# Feedback List View
def Feedbacklist(request):
    patients = Feedback.objects.all()
    return render(request, 'feedback.html', {'patientsdetail': patients})

