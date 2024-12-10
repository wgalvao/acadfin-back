from rest_framework import viewsets
from .models import Aliquota
from .serializers import AliquotaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AliquotaViewSet(viewsets.ModelViewSet):
    queryset = Aliquota.objects.all()
    serializer_class = AliquotaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        aliquotas = Aliquota.objects.filter(user_id=user_id)
        serializer = self.get_serializer(aliquotas, many=True)
        return Response(serializer.data)
