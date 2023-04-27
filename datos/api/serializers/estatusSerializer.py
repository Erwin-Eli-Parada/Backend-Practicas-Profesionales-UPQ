from rest_framework import serializers

from datos.models import EstatusResidencia

from datos.api.serializers.proyectoSerializer import ProyectoSerializer

class EstatusSerializer(serializers.ModelSerializer):
    id_practica = ProyectoSerializer()

    class Meta:
        model = EstatusResidencia
        fields = '__all__'