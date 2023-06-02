from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters
from datos.api.serializers.alumnoSerializer import AlumnoSerializer
import json

from datos.models import Alumno
from datos.models import Encuesta

@api_view(['GET'])
def graficoContratoView(request):
    if request.method == 'GET':
        
        siContrato = Alumno.objects.filter(id_practica__id_asesor_ext__encuesta__valor_descripcion="SI").filter(id_practica__id_asesor_ext__encuesta__pregunta="¿El alumno será contratado al término de su Estadia?").filter(id_practica__id_practica__tipo_proceso = 'Estadia').count() 

        noContrato = Alumno.objects.filter(id_practica__id_asesor_ext__encuesta__valor_descripcion="NO").filter(id_practica__id_asesor_ext__encuesta__pregunta="¿El alumno será contratado al término de su Estadia?").filter(id_practica__id_practica__tipo_proceso = 'Estadia').count() 

        respuesta = {
            "SI": siContrato,
            "NO": noContrato
        }
        
        return Response(respuesta, status= status.HTTP_200_OK)
    
