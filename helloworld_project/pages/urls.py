from django.urls import path

from .views import *

urlpatterns = [
    path('', home.as_view(), name = "home"),
    path('publication/add', PublicationAdd.as_view(), name="pub_add"),
    path('publication/<int:id>', PublicationUpdate.as_view(), name="pub_update"),
]