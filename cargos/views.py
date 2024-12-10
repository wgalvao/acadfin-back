from rest_framework import viewsets
from .models import Cargo
from .serializers import CargoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    
    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        cargos = Cargo.objects.filter(user_id=user_id)
        serializer = self.get_serializer(cargos, many=True)
        return Response(serializer.data)
