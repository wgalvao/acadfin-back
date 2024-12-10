from rest_framework import viewsets
from .models import Fornecedor
from .serializers import FornecedorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        fornecedores = Fornecedor.objects.filter(user_id=user_id)
        serializer = self.get_serializer(fornecedores, many=True)
        return Response(serializer.data)
