from rest_framework import serializers

from datos.models import Alumno, AsesorUPQ, AsesorExterno, Empresa, EstatusResidencia, Proyecto, Encuesta

from datos.api.serializers.proyectoSerializer import ProyectoSerializer
from datos.api.serializers.alumnoSerializer import AlumnoSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer
from datos.api.serializers.asesorUPQSerializer import AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer
from datos.api.serializers.estatusSerializer import EstatusSerializer
from datos.api.serializers.encuestaSerializer import EncuestaSerializer

class DatosSerializer(serializers.Serializer):
    alumno = serializers.SerializerMethodField()
    asesorUPQ = serializers.SerializerMethodField()
    asesorExterno = serializers.SerializerMethodField()
    empresa = serializers.SerializerMethodField()
    estatus = serializers.SerializerMethodField()
    proyecto = serializers.SerializerMethodField()
    encuesta = serializers.SerializerMethodField()

    def get_alumno(self, obj):
        alumno_queryset = Alumno.objects.filter(my_model=obj)
        return AlumnoSerializer(alumno_queryset, many=True).data
    
    def get_asesorUPQ(self, obj):
        asesorUPQ_queryset = AsesorUPQ.objects.filter(my_model=obj)
        return AsesorUPQSerializer(asesorUPQ_queryset, many=True).data
    
    def get_asesorExterno(self, obj):
        asesorExterno_queryset = AsesorExterno.objects.filter(my_model=obj)
        return AsesorExternoSerializer(asesorExterno_queryset, many=True).data
    
    def get_empresa(self, obj):
        empresa_queryset = Empresa.objects.filter(my_model=obj)
        return EmpresaSerializer(empresa_queryset, many=True).data

    def get_estatus(self, obj):
        estatus_queryset = EstatusResidencia.objects.filter(my_model=obj)
        return EstatusSerializer(estatus_queryset, many=True).data
    
    def get_proyecto(self, obj):
        proyecto_queryset = Proyecto.objects.filter(my_model=obj)
        return ProyectoSerializer(proyecto_queryset, many=True).data
    
    def get_encuesta(self, obj):
        encuesta_queryset = Encuesta.objects.filter(my_model=obj)
        return EncuestaSerializer(encuesta_queryset, many=True).data