from datos.models import AsesorExterno

from rest_framework import serializers

class AsesorExternoSerializer(serializers.ModelSerializers):

    class Meta:
        model = AsesorExterno
        fields = '__all__'
        read_only_fields = ('id_asesor_ext',)