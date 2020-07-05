from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects':projects})

def project1(request):
    return render(request, 'projects/nypd.html')

def project2(request):
    return render(request, 'projects/telco.html')

def project3(request):
    return render(request, 'projects/cred.html')

def project4(request):
    return render(request, 'projects/countries.html')

def project6(request):
    return render(request, 'projects/tmdb.html')