from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'estado', 'created_at')
