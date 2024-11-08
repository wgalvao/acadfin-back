from rest_framework import viewsets
from .models import CadServico
from .serializers import CadServicoSerializer


class CadServicoViewSet(viewsets.ModelViewSet):
    queryset = CadServico.objects.all()
    serializer_class = CadServicoSerializer
