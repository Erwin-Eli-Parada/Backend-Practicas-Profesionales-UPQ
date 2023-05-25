from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoTamanioView(request):
    if request.method == 'GET':
        g = 0
        m = 0
        mc = 0
        p = 0

        g = Alumno.objects.filter(id_practica__id_empresa__tamanio = 'G').count()
        m = Alumno.objects.filter(id_practica__id_empresa__tamanio = 'M').count()
        mc = Alumno.objects.filter(id_practica__id_empresa__tamanio = 'MC').count()
        p = Alumno.objects.filter(id_practica__id_empresa__tamanio = 'P').count()

        if g == None or m==None or mc==None or p==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        respuesta = {
            'g': g,
            'm': m,
            'mc': mc,
            'p': p
        }
        return Response( respuesta, status= status.HTTP_200_OK) 