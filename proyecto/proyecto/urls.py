from django.contrib import admin
from django.urls import path
from proyecto.views import inicio, registro, valida_login, lista_usuarios, crear_usuario, editar_usuario, eliminar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Vistas generales
    path('inicio/', inicio, name='inicio'),

    # registro
    path('registro/', registro, name='registro'),
    
    # CRUD de usuarios
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
    
    # Vistas relacionadas con el login
    path('valida_login/', valida_login, name='valida_login'),
]
