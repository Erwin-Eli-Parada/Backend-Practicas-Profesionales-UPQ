from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioAgregarSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = Usuario.objects.all()
        users_serializer = UsuarioSerializer(users, many=True)
        return Response(users_serializer.data)
    
    elif request.method == 'POST':
        users_serializer = UsuarioAgregarSerializer(data = request.data)
        if(users_serializer.is_valid()):
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors)

@api_view(['GET'])
def user_login_view(request,correo=None, password=None):
    user = Usuario.objects.filter(email = correo, password = password).first()
    user_serializer = UsuarioSerializer(user)
    return Response(user_serializer.data)

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk=None):
    if request.method == 'GET':
        user = Usuario.objects.filter(id = pk).first()
        user_serializer = UsuarioSerializer(user)
        return Response(user_serializer.data)
    
    elif request.method == 'PUT':
        user = Usuario.objects.filter(id=pk).first()
        user_serializer = UsuarioSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    
    elif request.method == 'DELETE':
        user = Usuario.objects.filter(id=pk).first()
        user.delete()
        return Response('Eliminado')