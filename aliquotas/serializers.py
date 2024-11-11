from rest_framework import serializers
from .models import Aliquota


class AliquotaSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Aliquota
        fields = ['id', 'tipo_imposto', 'percentual', 'estado', 'descricao',
                  'data_inicio', 'data_fim', 'created_at', 'updated_at', 'user_id']

    # def create(self, validated_data):
    #     validated_data['user_id'] = self.context['request'].user
    #     return super().create(validated_data)
