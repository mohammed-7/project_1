# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"app/index.html")

def navbar(request):
    return render(request,"app/navbar.html")

def navbar(request):
    return render(request,"app/carousel.html")