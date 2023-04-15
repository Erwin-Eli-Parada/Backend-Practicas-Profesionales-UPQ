from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id',)

class UsuarioAgregarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_email(self, value):
        print(value)
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya existe")
        return value
    
    def validate_username(self, value):
        print(value)
        if Usuario.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este usuario ya existe")
        return value