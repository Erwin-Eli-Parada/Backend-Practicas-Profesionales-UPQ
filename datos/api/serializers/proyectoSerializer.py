from rest_framework import serializers

from datos.models import Proyecto

from datos.api.serializers.asesorUPQSerializer import AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer
from datos.api.serializers.estatusSerializer import EstatusSerializer

class ProyectoSerializer(serializers.ModelSerializer):
    id_asesor = AsesorUPQSerializer()
    id_empresa = EmpresaSerializer()
    id_asesor_ext = AsesorExternoSerializer()
    id_practica = EstatusSerializer()

    class Meta:
        model = Proyecto
        fields = '__all__'