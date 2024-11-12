from rest_framework import viewsets
from .models import PlanoContas
from .serializers import PlanoContasSerializer


class PlanoContasViewSet(viewsets.ModelViewSet):
    queryset = PlanoContas.objects.all()
    serializer_class = PlanoContasSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
