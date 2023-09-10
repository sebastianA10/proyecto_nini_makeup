# myapp/forms.py
from django import forms
from .models import Usuarios



class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'estado']
