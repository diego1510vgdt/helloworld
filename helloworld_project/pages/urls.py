from django.urls import path

from .views import *

urlpatterns = [
    #path('', homePageView, name="home")
    path('', home.as_view(), name = "home")
]