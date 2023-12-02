from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    celular = models.BigIntegerField()
    email = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    contrasena = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    estado_usuarios_id = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'usuarios'


class empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    celular = models.BigIntegerField()
    genero = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    cargo_id = models.IntegerField(default=1)
    estado_empleados_id = models.IntegerField(default=1)
    

    class Meta:
        managed = False
        db_table = 'empleados'




class ProductosRegistro(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_registro'
       


