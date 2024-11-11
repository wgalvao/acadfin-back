from rest_framework import viewsets
from .models import BaseCalculo
from .serializers import BaseCalculoSerializer


class BaseCalculoViewSet(viewsets.ModelViewSet):
    queryset = BaseCalculo.objects.all()
    serializer_class = BaseCalculoSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)
