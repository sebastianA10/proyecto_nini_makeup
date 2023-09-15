from django.contrib import admin
from .models import Usuarios, Administrador

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'estado', 'created_at')

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('id','nombres', 'apellidos', 'email', 'celular', 'genero', 'contrasena')

# Register the model with the custom admin class
admin.site.register(Administrador, AdministradorAdmin)