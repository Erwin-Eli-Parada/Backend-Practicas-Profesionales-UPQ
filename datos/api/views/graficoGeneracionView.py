from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
import json

from datos.models import Alumno

@api_view(['GET'])
def graficoGeneracionView(request):
    if request.method == 'GET':
        
        registros_agrupados = Alumno.objects.values('generacion').annotate(cantidad=Count('generacion'))

        if registros_agrupados == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        objeto_json = []
        for registro in registros_agrupados:
            objeto = {
                "generacion": registro['generacion'],
                "cantidad": registro['cantidad'],
             # Agrega los campos que necesites
            }
            objeto_json.append(objeto)
        
        return Response(objeto_json, status= status.HTTP_200_OK) 