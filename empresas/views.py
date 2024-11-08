from django.shortcuts import render
# empresas/views.py
from rest_framework import viewsets
from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework.permissions import IsAuthenticated

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [IsAuthenticated]  # Protege a API com autenticação por token

# Create your views here.
