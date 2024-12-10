from rest_framework import serializers
from .models import Conta


class ContaSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Conta
        fields = ['id', 'conta', 'tipo_conta', 'descricao',
                  'saldo', 'created_at', 'updated_at', 'user_id']
