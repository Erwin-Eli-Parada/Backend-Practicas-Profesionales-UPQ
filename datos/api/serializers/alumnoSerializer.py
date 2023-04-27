from rest_framework import serializers

from datos.models import Alumno

from datos.api.serializers.proyectoSerializer import ProyectoSerializer

class AlumnoSerializer(serializers.ModelSerializer):
    id_practica = ProyectoSerializer()

    class Meta:
        model = Alumno
        fields = '__all__'