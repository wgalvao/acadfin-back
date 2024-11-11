from rest_framework import viewsets
from .models import Aliquota
from .serializers import AliquotaSerializer


class AliquotaViewSet(viewsets.ModelViewSet):
    queryset = Aliquota.objects.all()
    serializer_class = AliquotaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
