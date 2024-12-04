from rest_framework import viewsets
from .models import Cfop
from .serializers import CfopSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CfopViewSet(viewsets.ModelViewSet):
    queryset = Cfop.objects.all()
    serializer_class = CfopSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        cfpo = Cfop.objects.filter(user_id=user_id)
        serializer = self.get_serializer(cfpo, many=True)
        return Response(serializer.data)
