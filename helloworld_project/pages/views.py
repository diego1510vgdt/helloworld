from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Publication, Autor, Comment

# Create your views here.

#def homePageView(request):
#    return render (request, 'index.html', {})

class home(View):
    def get(self, request):
        publicaciones = Publication.objects.all()

        for pub in publicaciones:
            print(pub)
        
        context = {'publicaciones': publicaciones}
        return render(request, 'index.html', context)