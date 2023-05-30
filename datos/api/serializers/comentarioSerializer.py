from rest_framework import serializers

from datos.models import Comentario

# from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer

class ComentarioSerializer(serializers.ModelSerializer):
    # id_asesor_ext = AsesorExternoSerializer()

    class Meta:
        model = Comentario
        fields = '__all__'
        read_only_fields = ('id_encuesta',)