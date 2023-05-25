from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoGiroView(request):
    if request.method == 'GET':
        investigacion = 0
        privada = 0
        publica = 0
        social = 0

        investigacion = Alumno.objects.filter(id_practica__id_empresa__giro = 'investigacion').count()
        privada = Alumno.objects.filter(id_practica__id_empresa__giro = 'privada').count()
        publica = Alumno.objects.filter(id_practica__id_empresa__giro = 'publica').count()
        social = Alumno.objects.filter(id_practica__id_empresa__giro = 'social').count()

        if investigacion == None or privada==None or publica==None or social==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        respuesta = {
            'investigacion': investigacion,
            'privada': privada,
            'publica': publica,
            'social': social
        }
        return Response( respuesta, status= status.HTTP_200_OK)