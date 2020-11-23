from django.contrib import admin
from .models import Autor, Publication, Comments

# Register your models here.

admin.site.register(Autor)
admin.site.register(Publication)
admin.site.register(Comments)