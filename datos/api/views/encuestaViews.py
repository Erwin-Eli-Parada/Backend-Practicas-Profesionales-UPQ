from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from datos.models import Encuesta

from datos.api.serializers.encuestaSerializer import EncuestaSerializer

class EncuestaViewSet(viewsets.ModelViewSet):
    serializer_class = EncuestaSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def list(self,request):
        alumno_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(alumno_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Encuesta creada correctamente!'}, status = status.HTTP_201_CREATED)   
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            alumno_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if alumno_serializer.is_valid():
                alumno_serializer.save()
                return Response(alumno_serializer.data,status = status.HTTP_200_OK)
            return Response(alumno_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        alumno = self.get_queryset().filter(id = pk).first()
        if alumno:
            alumno.delete()
            return Response({'message':'Encuesta eliminada correctamente'},status = status.HTTP_200_OK)
        return Response({'error':'No existe'},status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def encuesta_detail_view(request, pk=None):
    if request.method == 'GET':
        encuesta = Encuesta.objects.filter(id_alumno = pk).all()
        if encuesta==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        encuesta_serializer = EncuestaSerializer(encuesta, many=True)
        return Response(encuesta_serializer.data, status= status.HTTP_200_OK)