from rest_framework import serializers

from datos.models import Proyecto

from datos.api.serializers.asesorUPQSerializer import AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer
from datos.api.serializers.estatusSerializer import EstatusSerializer

class ProyectoSerializer(serializers.ModelSerializer):
    fecha_solicitud = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    id_asesor = AsesorUPQSerializer()
    id_empresa = EmpresaSerializer()
    id_asesor_ext = AsesorExternoSerializer()
    id_practica = EstatusSerializer()

    class Meta:
        model = Proyecto
        fields = '__all__'


class ProyectoCrearSerializer(serializers.ModelSerializer):
    fecha_solicitud = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Proyecto
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id_practica':instance.id_practica.tipoproceso,
            'nombre_proyecto':instance.nombre_proyecto,
            'fecha_solicitud':instance.fecha_solicitud,
            'metodo_conocimiento':instance.metodo_conocimiento,
            'calificacion':instance.calificacion,
            'comentarios_finales':instance.comentarios_finales,
            'id_asesor':instance.id_asesor.nombre,
            'id_empresa':instance.id_empresa.nombre_empresa,
            'id_asesor_ext':instance.id_asesor_ext.nombre_asesor_ext
        }