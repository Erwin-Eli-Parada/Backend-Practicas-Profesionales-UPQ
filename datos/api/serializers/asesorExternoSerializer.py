from datos.models import AsesorExterno

from rest_framework import serializers

from datos.api.serializers.encuestaSerializer import EncuestaSerializer

class AsesorExternoSerializer(serializers.ModelSerializer):
    encuesta = EncuestaSerializer(many=True, read_only=True)

    class Meta:
        model = AsesorExterno
        fields = '__all__'
        read_only_fields = ('id_asesor_ext',)