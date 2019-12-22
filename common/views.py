from django.shortcuts import HttpResponse, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.schemas.openapi import AutoSchema

import coreapi
from common.serializers import UserRegisterSerializer
from common.models import User
from django.contrib.auth import authenticate, login, logout


class CustomSchema(AutoSchema):
    def get_operation(self, path, method, *args, **kwargs):
        import pdb
        pdb.set_trace()
        pass


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        AllowAny
    ]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


@api_view(['POST', ])
def login_view(request):
    # ----- YAML below for Swagger -----
    """
    description: This API deletes/uninstalls a device.
    parameters:
    - name: name
        type: string
        required: true
        location: form
    - name: bloodgroup
        type: string
        required: true
        location: form
    - name: birthmark
        type: string
        required: true
        location: form
    """
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)
    if user and user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'username': user.username,
            'email': user.email,
            'token': token.key
        }, status=status.HTTP_200_OK)
    elif user and not user.is_active:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', ])
def logout_view(request):
    user = request.user
    token = Token.objects.filter(user=user).delete()
    return Response({}, status=status.HTTP_200_OK)
