from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = Usuario.objects.all()
        users_serializer = UsuarioSerializer(users, many=True)
        return Response(users_serializer.data)
    
    elif request.method == 'POST':
        users_serializer = UsuarioSerializer(data = request.data)
        if(users_serializer.is_valid()):
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors)

@api_view(['GET'])
def user_detail_view(request,nombre=None):
    user = Usuario.objects.filter(username = nombre).first()
    user_serializer = UsuarioSerializer(user)
    return Response(user_serializer.data)