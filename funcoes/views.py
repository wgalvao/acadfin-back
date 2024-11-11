from rest_framework import viewsets
from .models import Funcao
from .serializers import FuncaoSerializer


from rest_framework import generics
from .models import Funcao
from .serializers import FuncaoSerializer


class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer


# class FuncaoListView(generics.ListAPIView):
#     # Usa select_related para otimizar a consulta
#     queryset = Funcao.objects.select_related('empresa').all()
#     serializer_class = FuncaoSerializer


# class FuncaoDetailView(generics.RetrieveAPIView):
#     queryset = Funcao.objects.select_related('empresa').all()
#     serializer_class = FuncaoSerializer
