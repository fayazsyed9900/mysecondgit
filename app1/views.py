from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fayaz(request):
    return HttpResponse('<marquee>its my name fayaz<marquee>')