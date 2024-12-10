from rest_framework import viewsets
from .models import CadServico
from .serializers import CadServicoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CadServicoViewSet(viewsets.ModelViewSet):
    queryset = CadServico.objects.all()
    serializer_class = CadServicoSerializer

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        services = CadServico.objects.filter(user_id=user_id)
        serializer = self.get_serializer(services, many=True)
        return Response(serializer.data)
