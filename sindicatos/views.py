from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import CadSindicato
from .serializers import CadSindicatoSerializer


class CadSindicatoViewSet(viewsets.ModelViewSet):
    queryset = CadSindicato.objects.all()
    serializer_class = CadSindicatoSerializer


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
