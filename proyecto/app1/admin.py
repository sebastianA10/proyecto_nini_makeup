from django.contrib import admin
from app1.models import Usuarios, empleados, Productos

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena','created_at','estado_usuarios_id')

class empleadosAdmin(admin.ModelAdmin):
    list_display = ('id','nombres', 'apellidos', 'email', 'celular', 'genero', 'contrasena', 'cargo_id', 'estado_empleados_id')


# Register the model with the custom admin class
# admin.site.register(empleados, empleadosAdmin, Productos)
admin.site.register(Productos)