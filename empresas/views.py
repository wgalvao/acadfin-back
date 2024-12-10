from django.shortcuts import render
# empresas/views.py
from rest_framework import viewsets
from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [IsAuthenticated]  # Protege a API com autenticação por token

# Create your views here.

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        empresas = Empresa.objects.filter(user_id=user_id)
        serializer = self.get_serializer(empresas, many=True)
        return Response(serializer.data)
