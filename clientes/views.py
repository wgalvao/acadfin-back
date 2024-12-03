from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)
    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        clientes = Cliente.objects.filter(user_id=user_id)
        serializer = self.get_serializer(clientes, many=True)
        return Response(serializer.data)
