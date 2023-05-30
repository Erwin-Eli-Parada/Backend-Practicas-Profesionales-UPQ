from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from datos.api.serializers.asesorExternoSerializer import AsesorExternoIdSerializer
from datos.api.serializers.comentarioSerializer import ComentarioSerializer
from datos.api.serializers.alumnoSerializer import AlumnoSerializer
import pandas as pd
import math

class ExcelComentarioViewSet(viewsets.ModelViewSet):
    def create(self,request):
        archivo = request.FILES.get('archivo')
        data = pd.read_excel(archivo, dtype={'Matricula': str})
        df = pd.DataFrame(data)
        
        for i in range(len(data)):
            matricula_df = "0"+str(df.at[i, 'Matricula']) if len(str(df.at[i, 'Matricula']))<9 else str(df.at[i, 'Matricula'])
            alumno = AlumnoSerializer.Meta.model.objects.filter(matricula=matricula_df).first()
            if alumno is not None:
                asesorext = AsesorExternoIdSerializer.Meta.model.objects.filter(nombre_asesor_ext=str(df.at[i, 'Nombre Asesor Externo'])).first()
                if asesorext is not None:
                    id_asesor = asesorext.id_asesor_ext
                    dataR = {
                        "pregunta":str(df.at[i, 'Pregunta']),
                        "comentario":str(df.at[i, 'Comentario']),
                        "id_asesor_ext":id_asesor,
                        "id_alumno":matricula_df
                    }
                    print(dataR)
                    serializer = ComentarioSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
        return Response({'mensaje':'Agregado correctamente'}, status = status.HTTP_201_CREATED)  