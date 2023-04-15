from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
class Usuario(AbstractUser):
    username = models.CharField('Nombre de usuario', unique=False, max_length=100)
    email = models.EmailField('Correo Electronico', unique=False, max_length=254)
    nombre = models.CharField('Nombre', unique=False, max_length=200, blank=True, null= True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['username','password']
