from django.contrib import admin
from .models import Autor, Publication, Comment

# Register your models here.

admin.site.register(Autor)
admin.site.register(Publication)
admin.site.register(Comment)