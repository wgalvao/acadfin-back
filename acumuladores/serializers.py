from rest_framework import serializers
from .models import Acumulador


class AcumuladorSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Acumulador
        fields = ['id', 'acumulador', 'tipo', 'descricao',
                  'valor', 'created_at', 'updated_at', 'user_id']

    # def create(self, validated_data):
    #     validated_data['user_id'] = self.context['request'].user
    #     return super().create(validated_data)
