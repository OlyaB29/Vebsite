from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'main/index.html')

def contacts(request):
    return HttpResponse("<h1>Contacts</h1>")

def about(request):
    return render(request,'main/about.html')

def tasks(request):
    return HttpResponse("<h1>Our tasks</h1>")


