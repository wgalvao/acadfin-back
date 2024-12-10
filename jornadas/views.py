from rest_framework import viewsets
from .models import Jornada
from .serializers import JornadaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class JornadaViewSet(viewsets.ModelViewSet):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        jornadas = Jornada.objects.filter(user_id=user_id)
        serializer = self.get_serializer(jornadas, many=True)
        return Response(serializer.data)
