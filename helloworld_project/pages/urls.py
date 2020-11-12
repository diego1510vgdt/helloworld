from django.urls import path

from .views import homePageView
from comments.views import commentsView
from about.views import aboutView

urlpatterns = [
    path('', homePageView, name="home")
]