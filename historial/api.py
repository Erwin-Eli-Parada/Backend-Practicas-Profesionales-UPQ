from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status  
from .models import Historial
from .serializers import HistorialSerializer, AgregarHistorialSerializer

@api_view(['GET','POST'])
def historial_api_view(request):
    if request.method == 'GET':
        historial = Historial.objects.all()
        historial_serializer = HistorialSerializer(historial, many=True)
        return Response(historial_serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        historial_serializer = AgregarHistorialSerializer(data = request.data)
        if(historial_serializer.is_valid()):
            historial_serializer.save()
            return Response(historial_serializer.data, status= status.HTTP_201_CREATED)
        return Response(historial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)