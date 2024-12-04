from rest_framework import viewsets
from .models import Funcao
from .serializers import FuncaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer


    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        funcoes = Funcao.objects.filter(user_id=user_id)
        serializer = self.get_serializer(funcoes, many=True)
        return Response(serializer.data)
