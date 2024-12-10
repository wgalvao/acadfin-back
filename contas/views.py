from rest_framework import viewsets
from .models import Conta
from .serializers import ContaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        contas = Conta.objects.filter(user_id=user_id)
        serializer = self.get_serializer(contas, many=True)
        return Response(serializer.data)
