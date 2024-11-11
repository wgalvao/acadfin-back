from rest_framework import viewsets
from .models import Funcao
from .serializers import FuncaoSerializer


class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)
