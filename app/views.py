from django.shortcuts import render,redirect
from . models import Departments
# Create your views here.

def MainPage(request):
   
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Department(request):
    departments=Departments.objects.all()
    return render(request, 'departments.html',{'departments':departments})

def Create_dpt(request):
    if request.method == 'POST':
        dep_name=request.POST.get('dep_name')
        dep_description=request.POST.get('dep_description')
        print(dep_name,dep_description)

        Departments.objects.create(dep_name=dep_name,dep_description=dep_description)

        return redirect('home')

    return render(request, 'create.html')

def Contact(request):
    return render(request, 'contact.html')