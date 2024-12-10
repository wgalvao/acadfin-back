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
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    # Bloqueia o acesso as rotas desta API sem a utilização de token
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        funcionarios = Funcionario.objects.filter(user_id=user_id)
        serializer = self.get_serializer(funcionarios, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def list_by_empresa(self, request, empresa_id=None):
        funcionarios = Funcionario.objects.filter(empresa_id=empresa_id)
        serializer = self.get_serializer(funcionarios, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_salario_meses_trabalhados(self, request, pk=None):
        funcionario = self.get_object()
        salario = funcionario.cargo.salario if funcionario.cargo else None
        meses_trabalhados = None
        if funcionario.created_at:
            created_at = funcionario.created_at.replace(tzinfo=None)
            now = datetime.now()
            meses_trabalhados = (now.year - created_at.year) * \
                12 + (now.month - created_at.month)
        return Response({"salario": salario, "meses_trabalhados": meses_trabalhados})
