from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from datos.api.serializers.datosSerializer import DatosSerializer

from datos.models import Alumno, AsesorUPQ, AsesorExterno, Empresa, EstatusResidencia, Proyecto, Encuesta

class DatosViewSet(viewsets.ModelViewSet):
    serializer_class = DatosSerializer
    

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def list(self,request):
        datos_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(datos_serializer.data,status = status.HTTP_200_OK)