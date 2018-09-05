from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response

from user.models import User, Products
from user.serializer import UserSerializer, ProductSerializer
import jwt, json


class Login(views.APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': 'Por favor, escriba su usuario y clave'}, status=400)
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Usuario y/o contraseña invalidos"}, status=400)

        if user:
            payload = UserSerializer(user).data
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return Response(jwt_token, status=200, content_type="application/json")
        else:
            return Response(json.dumps({'Error': "Invalid credentials"}), status=400, content_type="application/json")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
