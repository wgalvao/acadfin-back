from rest_framework import viewsets
from .models import BaseCalculo
from .serializers import BaseCalculoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BaseCalculoViewSet(viewsets.ModelViewSet):
    queryset = BaseCalculo.objects.all()
    serializer_class = BaseCalculoSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)
    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        baseCalculo = BaseCalculo.objects.filter(user_id=user_id)
        serializer = self.get_serializer(baseCalculo, many=True)
        return Response(serializer.data)
