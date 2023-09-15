from django import forms
from .models import Usuarios, Administrador

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'estado']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombres', 'apellidos', 'email', 'celular', 'genero','contrasena']
