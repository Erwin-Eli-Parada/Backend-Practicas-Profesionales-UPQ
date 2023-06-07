from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id',)

class UsuarioAgregarSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.password = make_password(password)
        user.save()
        return user
    
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
    
class UsuarioActualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_email(self, value):
        print(value)
        if Usuario.objects.filter(email=value).exclude(id=self.context).exists():
            raise serializers.ValidationError("Este correo electrónico ya existe")
        return value
    
    def validate_username(self, value):
        print(value)
        if Usuario.objects.filter(username=value).exclude(id=self.context).exists():
            raise serializers.ValidationError("Este usuario ya existe")
        return value