from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<center><h2>Hi, I am Praful Sharma</h2>")
