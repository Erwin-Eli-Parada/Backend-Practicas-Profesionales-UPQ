from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status  
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioAgregarSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = Usuario.objects.all()
        users_serializer = UsuarioSerializer(users, many=True)
        return Response(users_serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        users_serializer = UsuarioAgregarSerializer(data = request.data)
        if(users_serializer.is_valid()):
            users_serializer.save()
            return Response(users_serializer.data, status= status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_login_view(request,correo=None, password=None):
    user = Usuario.objects.filter(email = correo, password = password).first()
    user_serializer = UsuarioSerializer(user)
    if user==None:
        return Response(user_serializer.data, status=status.HTTP_401_UNAUTHORIZED)
    return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk=None):
    if request.method == 'GET':
        user = Usuario.objects.filter(id = pk).first()
        if user==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_serializer = UsuarioSerializer(user)
        return Response(user_serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        user = Usuario.objects.filter(id=pk).first()
        user_serializer = UsuarioSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status= status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user = Usuario.objects.filter(id=pk).first()
        if user==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response('Eliminado', status= status.HTTP_200_OK)