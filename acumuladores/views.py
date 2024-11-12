from rest_framework import viewsets
from .models import Acumulador
from .serializers import AcumuladorSerializer


class AcumuladorViewSet(viewsets.ModelViewSet):
    queryset = Acumulador.objects.all()
    serializer_class = AcumuladorSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
