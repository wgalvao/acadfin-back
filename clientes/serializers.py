from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'desde', 'taxa_desconto', 'limite_credito',
                  'observacao', 'created_at', 'updated_at', 'user_id']
