from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoTipoView(request):
    if request.method == 'GET':
        estadia = 0
        estancia1 = 0
        estancia2 = 0

        estadia = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estadia').count()
        estancia1 = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia I').count()
        estancia2 = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia II').count()

        if estadia == None or estancia1==None or estancia2==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        respuesta = {
            'estadia': estadia,
            'estancia1': estancia1,
            'estancia2': estancia2
        }
        return Response( respuesta, status= status.HTTP_200_OK)