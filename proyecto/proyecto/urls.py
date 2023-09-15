from django.contrib import admin
from django.urls import path
from proyecto.views import inicio, registro, valida_login, lista_usuarios, crear_usuario, editar_usuario, eliminar_usuario, administrador, registro_administrador

urlpatterns = [

    # url administrador
    path('admin/', admin.site.urls),
    
    # url pagina principal
    path('inicio/', inicio, name='inicio'),

    # registro usuarios
    path('registro/', registro, name='registro'),
    
    # url crud de usuarios
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
    
    # url login usuarios
    path('valida_login/', valida_login, name='valida_login'),
    
    # url login administrador
     path('administrador/', administrador, name='administrador'),

    # url registro addministrador
     path('registro_administrador/', registro_administrador, name='registro_administrador'),   
]
