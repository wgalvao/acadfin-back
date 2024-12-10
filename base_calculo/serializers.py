from rest_framework import serializers
from .models import BaseCalculo


class BaseCalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCalculo
        fields = ['id', 'nome', 'descricao', 'tipo', 'percentual', 'valor_minimo',
                  'valor_maximo', 'ativo', 'created_at', 'updated_at', 'user_id']
