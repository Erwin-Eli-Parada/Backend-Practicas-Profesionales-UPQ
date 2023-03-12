from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username', 'email', 'nombre', 'usuario_administrador', 'staff', 'password')
        read_only_fields = ('id')