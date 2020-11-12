from django.urls import path

from .views import commentsView
from about.views import aboutView

urlpatterns = [
    path('', commentsView, name="comments")
]