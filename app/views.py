from django.shortcuts import render,redirect
from . models import Departments
from . models import Doctors
from .form import BookingForm
from . models import Booking
# Create your views here.

def MainPage(request):
    return render(request, 'index.html')

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