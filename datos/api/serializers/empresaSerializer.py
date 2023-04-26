from datos.models import Empresa

from rest_framework import serializers

class EmpresaSerializer(serializers.ModelSerializers):

    class Meta:
        model = Empresa
        fields = '__all__'
        read_only_fields = ('id_empresa',)