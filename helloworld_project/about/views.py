from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutView(request):
    return HttpResponse('Esta es la app de about')