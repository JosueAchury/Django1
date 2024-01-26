from django.db import models

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'producto'

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=244)
    tipo_usuario = models.CharField(max_length=244)
    correo = models.CharField(max_length=244)
    username = models.CharField(max_length=244)
    clave = models.CharField(max_length=244)
    numero_telefono = models.CharField(max_length=10)
    token = models.CharField(max_length=12)

    class Meta:
        db_table = 'usuarios'