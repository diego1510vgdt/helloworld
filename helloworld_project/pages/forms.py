from django import forms
from .models import Autor,Publication,Comment

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['autor','titulo','contenido']