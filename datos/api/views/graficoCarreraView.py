from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoCarreraView(request):
    if request.method == 'GET':
        automotriz = 0
        manufactura = 0
        mecatronica = 0
        negocios = 0
        pymes = 0
        pymes_eje = 0
        sistemas = 0
        telematica = 0

        automotriz = Alumno.objects.filter(carrera = 'AUTOMOTRIZ').count()
        manufactura = Alumno.objects.filter(carrera = 'MANUFACTURA').count()
        mecatronica = Alumno.objects.filter(carrera = 'MECATRONICA').count()
        negocios = Alumno.objects.filter(carrera = 'NEGOCIOS').count()
        pymes = Alumno.objects.filter(carrera = 'PYMES').count()
        pymes_eje = Alumno.objects.filter(carrera = 'PYMES EJECUTIVA').count()
        sistemas = Alumno.objects.filter(carrera = 'SISTEMAS').count()
        telematica = Alumno.objects.filter(carrera = 'TELEMATICA').count()

        if automotriz == None or manufactura==None or mecatronica==None or negocios==None or pymes==None or pymes_eje==None or sistemas==None or telematica==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        respuesta = {
            "automotriz":automotriz,
            "manufactura":manufactura,
            "mecatronica":mecatronica,
            "negocios":negocios,
            "pymes":pymes,
            "pymes_eje":pymes_eje,
            "sistemas":sistemas,
            "telematica":telematica
        }
        return Response( respuesta, status= status.HTTP_200_OK)