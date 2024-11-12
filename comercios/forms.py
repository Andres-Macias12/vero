# albarrio/comercios/forms.py
from django import forms
from django.contrib.auth.models import User  
from .models import Comercio, Novedad

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = ['nombre', 'descripcion', 'categoria', 'direccion', 'contacto', 'redes_sociales', 'foto', 'novedad']

class NovedadForm(forms.ModelForm):
    class Meta:
        model = Novedad
        fields = ['titulo', 'descripcion', 'imagen', 'comercio']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
