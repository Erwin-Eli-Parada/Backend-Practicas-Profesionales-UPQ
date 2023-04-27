from rest_framework import serializers

from datos.models import Proyecto

from datos.api.serializers.asesorUPQSerializer import AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer

class ProyectoSerializer(serializers.ModelSerializer):
    id_asesor = AsesorUPQSerializer()
    id_empresa = EmpresaSerializer()
    id_asesor_ext = AsesorExternoSerializer()

    class Meta:
        model = Proyecto
        fields = '__all__'