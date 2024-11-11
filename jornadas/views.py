from rest_framework import viewsets
from .models import Jornada
from .serializers import JornadaSerializer


class JornadaViewSet(viewsets.ModelViewSet):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)
