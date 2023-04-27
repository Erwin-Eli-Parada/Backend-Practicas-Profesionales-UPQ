from datos.models import AsesorUPQ

from rest_framework import serializers

class AsesorUPQSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsesorUPQ
        fields = '__all__'
        read_only_fields = ('id_asesor',)