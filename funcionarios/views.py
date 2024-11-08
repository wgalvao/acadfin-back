from django.shortcuts import render

# Create your views here.python
"""
ViewSet for managing Funcionario instances.

This ViewSet provides CRUD operations for Funcionario objects,
utilizing the FuncionarioSerializer for data representation.
"""
from rest_framework import viewsets
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    # Bloqueia o acesso as rotas desta API sem a utilização de token
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
