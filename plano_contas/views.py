from rest_framework import viewsets
from .models import PlanoContas
from .serializers import PlanoContasSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PlanoContasViewSet(viewsets.ModelViewSet):
    queryset = PlanoContas.objects.all()
    serializer_class = PlanoContasSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        planoContas = PlanoContas.objects.filter(user_id=user_id)
        serializer = self.get_serializer(planoContas, many=True)
        return Response(serializer.data)
