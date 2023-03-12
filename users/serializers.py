from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username', 'email', 'nombre', 'is_superuser', 'is_staff', 'is_active', 'password')
        read_only_fields = ('id',)