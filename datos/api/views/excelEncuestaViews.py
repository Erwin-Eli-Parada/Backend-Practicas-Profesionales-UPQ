from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from datos.api.serializers.asesorExternoSerializer import AsesorExternoIdSerializer
from datos.api.serializers.encuestaSerializer import EncuestaSerializer
from datos.api.serializers.alumnoSerializer import AlumnoSerializer
import pandas as pd
import math

class ExcelEncuestasViewSet(viewsets.ModelViewSet):
    def create(self,request):
        archivo = request.FILES.get('archivo')
        data = pd.read_excel(archivo)
        df = pd.DataFrame(data)
        
        for i in range(len(data)):
            alumno = AlumnoSerializer.Meta.model.objects.filter(matricula=str(df.at[i, 'Matricula'])).first()
            if alumno is not None:
                asesorext = AsesorExternoIdSerializer.Meta.model.objects.filter(nombre_asesor_ext=str(df.at[i, 'Nombre Asesor Externo'])).first()
                if asesorext is not None:
                    id_asesor = asesorext.id_asesor_ext
                    dataR = {
                        "descripcion":str(df.at[i, 'Descripcion']),
                        "valor_descripcion":str(df.at[i, 'Valor Descripcion']),
                        "pregunta":str(df.at[i, 'Pregunta']),
                        "valor":str(df.at[i, 'Valor']),
                        "id_asesor_ext":id_asesor
                    }
                    serializer = EncuestaSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
        return Response({'mensaje':'Agregado correctamente'}, status = status.HTTP_201_CREATED)  