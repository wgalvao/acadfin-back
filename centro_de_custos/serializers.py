from rest_framework import serializers
from .models import CadCentroDeCustos


class CadCentroDeCustosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadCentroDeCustos
        fields = ['id', 'nome', 'descricao', 'codigo',
                  'ativo', 'created_at', 'updated_at']
