from rest_framework import serializers

from datos.models import Proyecto

from datos.api.serializers.asesorUPQSerializer import AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer

class ProyectoSerializer(serializers.ModelSerializers):
    id_asesor = AsesorUPQSerializer()
    id_empresa = EmpresaSerializer()

    class Meta:
        model = Proyecto
        fields = '__all__'