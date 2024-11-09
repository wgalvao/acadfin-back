from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CadCentroDeCustos
from .serializers import CadCentroDeCustosSerializer


class CadCentroDeCustosViewSet(viewsets.ModelViewSet):
    queryset = CadCentroDeCustos.objects.all()
    serializer_class = CadCentroDeCustosSerializer
