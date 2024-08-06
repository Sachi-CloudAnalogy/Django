from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello world !!")

def about(request):
    return HttpResponse("Hi world !!")

def next(request):
    return render(request, 'index.html')
