from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from datos.models import AsesorUPQ
from datos.models import Empresa
from datos.models import AsesorExterno
from datos.models import EstatusResidencia
from datos.api.serializers.asesorUPQSerializer import AsesorUPQIdSerializer, AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer
from datos.api.serializers.estatusSerializer import EstatusSerializer
import pandas as pd
import math

class ExcelViewSet(viewsets.ModelViewSet):
    def create(self,request):
        archivo = request.FILES.get('archivo')
        data = pd.read_excel(archivo)
        df = pd.DataFrame(data)
        asesorupq = ""
        id_asesorupq = 1

        #Datos del Asesor UPQ
        for i in range(len(data)):
            if str(df.at[i, 'Asesor UPQ']) != "nan":
                if not AsesorUPQ.objects.filter(nombre=str(df.at[i, 'Asesor UPQ'])).exists():
                    dataR = {"nombre":str(df.at[i, 'Asesor UPQ'])}
                    serializer = AsesorUPQSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                        # asesorupq = asesorupq + str(df.at[i, 'Asesor UPQ']) +"\n"

                asesor = AsesorUPQIdSerializer.Meta.model.objects.filter(nombre=str(df.at[i, 'Asesor UPQ'])).first()
                if asesor is not None:
                    id_asesorupq = asesor.id_asesor
                # print(str(id_asesorupq))

            #Datos de la Empresa
            if str(df.at[i,'Empresa']) != "nan":
                if not Empresa.objects.filter(nombre_empresa=str(df.at[i, 'Empresa'])).exists():
                    dataR = {
                        "nombre_empresa":str(df.at[i, 'Empresa']),
                        "sector":str(df.at[i, 'Sector']),
                        "giro":str(df.at[i, 'Giro']),
                        "tamanio":str(df.at[i, 'Tamaño']),
                        "correo":str(df.at[i, 'Correo RH Empresa']),
                        "telefono":str(df.at[i, 'Telefono RH Empresa'])
                    }
                    serializer = EmpresaSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()

            #Datos del Asesor Externo
            if str(df.at[i, 'Asesor Empresa']) != "nan":
                if not AsesorExterno.objects.filter(nombre_asesor_ext=str(df.at[i, 'Asesor Empresa'])).exists():
                    dataR = {"nombre_asesor_ext":str(df.at[i, 'Asesor Empresa'])}
                    serializer = AsesorExternoSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()

            #Datos de Estatus de la residencia
            

        # serializer = ProyectoCrearSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'mensaje':'Alumno creado correctamente!'}, status = status.HTTP_201_CREATED)   
        # return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':asesorupq}, status = status.HTTP_201_CREATED)