from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def education(request):
    return render(request, 'education.html')

def projects(request):
    return render(request, 'projects.html')

def achievements(request):
    return render(request, 'achievements.html')

def contact(request):
    return render(request, 'contact.html')