from django.db import models

# Create your models here.
class Historial(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField('id_usuario',blank=False, null=False)
    username = models.CharField('Nombre de usuario', unique=False, max_length=100)
    email = models.EmailField('Correo Electronico', unique=False, max_length=254)
    nombre = models.CharField('Nombre de usuario', unique=False, max_length=100)
    password = models.CharField('Password', unique=False, max_length=100, null=False, default="")
    rol = models.IntegerField('id_usuario',blank=False, null=False)
    usuario_elim = models.CharField('Nombre de usuario que elimina', unique=False, max_length=100)
    deleted_date = models.DateTimeField('Fecha de eliminacion', auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

