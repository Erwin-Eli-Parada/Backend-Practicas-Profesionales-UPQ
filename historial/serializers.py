from rest_framework import serializers
from .models import Historial

class HistorialSerializer(serializers.ModelSerializer):
    deleted_date = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S")

    class Meta:
        model = Historial
        fields = '__all__'
        read_only_fields = ('id','deleted_date')

class AgregarHistorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Historial
        fields = '__all__'
        read_only_fields = ('id',)