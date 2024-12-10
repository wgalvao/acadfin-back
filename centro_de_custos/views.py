from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CadCentroDeCustos
from .serializers import CadCentroDeCustosSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CadCentroDeCustosViewSet(viewsets.ModelViewSet):
    queryset = CadCentroDeCustos.objects.all()
    serializer_class = CadCentroDeCustosSerializer

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        centroCustos = CadCentroDeCustos.objects.filter(user_id=user_id)
        serializer = self.get_serializer(centroCustos, many=True)
        return Response(serializer.data)
