from rest_framework import viewsets
from .models import Cfop
from .serializers import CfopSerializer


class CfopViewSet(viewsets.ModelViewSet):
    queryset = Cfop.objects.all()
    serializer_class = CfopSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
