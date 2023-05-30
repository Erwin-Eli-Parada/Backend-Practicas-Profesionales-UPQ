from datos.models import AsesorExterno

from rest_framework import serializers

from datos.api.serializers.encuestaSerializer import EncuestaSerializer
from datos.api.serializers.comentarioSerializer import ComentarioSerializer

class AsesorExternoSerializer(serializers.ModelSerializer):
    encuesta = EncuestaSerializer(many=True, read_only=True)
    comentario = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = AsesorExterno
        fields = '__all__'
        read_only_fields = ('id_asesor_ext',)

class AsesorExternoIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsesorExterno
        fields = 'id_asesor_ext'
        read_only_fields = ('id_asesor_ext',)