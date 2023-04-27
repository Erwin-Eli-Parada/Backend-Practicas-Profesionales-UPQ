from datos.models import AsesorExterno

from rest_framework import serializers

from datos.api.serializers.empresaSerializer import EmpresaSerializer

class AsesorExternoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsesorExterno
        fields = '__all__'
        read_only_fields = ('id_asesor_ext',)