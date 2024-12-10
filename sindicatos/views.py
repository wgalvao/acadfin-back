from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import CadSindicato
from .serializers import CadSindicatoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
class CadSindicatoViewSet(viewsets.ModelViewSet):
    queryset = CadSindicato.objects.all()
    serializer_class = CadSindicatoSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        sindicatos = CadSindicato.objects.filter(user_id=user_id)
        serializer = self.get_serializer(sindicatos, many=True)
        return Response(serializer.data)
