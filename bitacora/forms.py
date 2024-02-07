
from django import forms
from .models import *

class bitacoraForm(forms.ModelForm):
    class Meta:
        model = bitacora
        exclude = ('usuario',)
        widgets = {
            'comentario' :       forms.Textarea(attrs={'rows':3, 'placeholder': ''}),
        }

from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Campos que deseas permitir editar en el perfil
