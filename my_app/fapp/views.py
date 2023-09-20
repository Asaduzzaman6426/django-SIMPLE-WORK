from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello world<h1/>")
def eco(request):
    return HttpResponse("<h1>Hello world checked asad<h1/>")
