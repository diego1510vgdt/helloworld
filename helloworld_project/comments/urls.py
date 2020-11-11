from django.urls import path

from .views import commentsView
from about.views import aboutView

urlpatterns = [
    path('comments/', commentsView, name="comments"),
    path('about/', aboutView, name="about")
]