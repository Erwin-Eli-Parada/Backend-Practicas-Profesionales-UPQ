from rest_framework import serializers

from datos.models import Alumno

from datos.api.serializers.proyectoSerializer import ProyectoSerializer

class AlumnoSerializer(serializers.ModelSerializer):
    id_practica = ProyectoSerializer() 

    class Meta:
        model = Alumno
        fields = '__all__'


class AlumnoCrearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumno
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'matricula':instance.matricula,
            'correo':instance.correo,
            'correo_institucional':instance.correo_institucional,
            'generacion':instance.generacion,
            'grupo':instance.grupo,
            'carrera':instance.carrera,
            'nss':instance.nss,
            'genero':instance.genero,
            'nombre':instance.nombre,
            'id_practica':instance.id_practica.nombre_proyecto
        }