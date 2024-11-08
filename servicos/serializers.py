from rest_framework import serializers
from .models import CadServico


class CadServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadServico
        fields = ['id', 'codigo', 'descricao', 'valor',
                  'created_at', 'updated_at', 'user_id']
