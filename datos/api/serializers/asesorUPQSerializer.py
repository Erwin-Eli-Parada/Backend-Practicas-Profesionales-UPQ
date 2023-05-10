from datos.models import AsesorUPQ

from rest_framework import serializers

class AsesorUPQSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsesorUPQ
        fields = '__all__'
        read_only_fields = ('id_asesor',)

class AsesorUPQIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsesorUPQ
        fields = 'id_asesor'
        read_only_fields = ('id_asesor',)