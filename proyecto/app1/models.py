from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    celular = models.BigIntegerField()
    email = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    contrasena = models.CharField(max_length=255)
    estado = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'usuarios'  # Especifica la tabla para este modelo

class empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    celular = models.BigIntegerField()
    genero = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'empleados'
