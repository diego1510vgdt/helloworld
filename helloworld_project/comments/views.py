from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def commentsView(request):
    return HttpResponse('Esta es la app de comments')