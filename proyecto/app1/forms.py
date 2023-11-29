from django import forms
from .models import Usuarios, empleados


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena']

class empleadosForm(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ['nombres', 'apellidos', 'email', 'celular', 'genero','contrasena']
