from rest_framework import serializers

from datos.models import Encuesta

from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer

class EncuestaSerializer(serializers.ModelSerializers):
    id_asesor_ext = AsesorExternoSerializer()

    class Meta:
        model = Encuesta
        fields = '__all__'
        read_only_fields = ('id_encuesta',)