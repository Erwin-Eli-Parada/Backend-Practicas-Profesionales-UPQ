from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoGeneroView(request):
    if request.method == 'GET':
        hombre = 0
        mujer = 0

        hombre = Alumno.objects.filter(genero = 'MASCULINO').count()
        mujer = Alumno.objects.filter(genero = 'FEMENINO').count()

        if hombre == None or mujer==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        respuesta = {
            'hombre': hombre,
            'mujer': mujer
        }
        return Response( respuesta, status= status.HTTP_200_OK)