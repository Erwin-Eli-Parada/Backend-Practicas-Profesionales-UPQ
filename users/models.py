from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class UsuarioManager(BaseUserManager):
#     def create_user(self, email, username, nombre, staff, password = None):
#         if not email:
#             raise ValueError('El usuario debe tener un correo electronico')
        
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#             nombre = nombre,
#             staff = staff
#         )

#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, username, email, nombre, password ,staff = True):
#         user = self.create_user(
#             username = username,
#             email = self.normalize_email(email),
#             nombre = nombre,
#             password=password
#         )

#         user.usuario_administradir = True
#         user.save()
#         return user
    
class Usuario(AbstractUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', unique=True, max_length=254)
    nombre = models.CharField('Nombre', unique=False, max_length=200, blank=True, null= True)
    # usuario_activo = models.BooleanField(default=True)
    # usuario_administrador = models.BooleanField(default=False)
    # staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    # def __str__(self):
    #     return f'{self.nombre}'
    
    # def has_perm(self,perm,ob = None):
    #     return True
    
    # def has_module_perms(self,app_label):
    #     return True
    
    # @property
    # def is_staff(self):
    #     return self.usuario_administrador