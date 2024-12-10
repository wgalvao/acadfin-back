from rest_framework import viewsets
from .models import Acumulador
from .serializers import AcumuladorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AcumuladorViewSet(viewsets.ModelViewSet):
    queryset = Acumulador.objects.all()
    serializer_class = AcumuladorSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        acumuladores = Acumulador.objects.filter(user_id=user_id)
        serializer = self.get_serializer(acumuladores, many=True)
        return Response(serializer.data)