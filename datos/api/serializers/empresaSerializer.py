from datos.models import Empresa

from rest_framework import serializers

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = '__all__'
        read_only_fields = ('id_empresa',)

class EmpresaIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = 'id_empresa'
        read_only_fields = ('id_empresa',)