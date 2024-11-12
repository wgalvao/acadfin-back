from rest_framework import serializers
from .models import PlanoContas


class PlanoContasSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PlanoContas
        fields = ['id', 'codigo_contas', 'nome_conta', 'tipo_conta', 'nivel',
                  'descricao', 'conta_pai', 'created_at', 'updated_at', 'user_id']

    # def create(self, validated_data):
    #     validated_data['user_id'] = self.context['request'].user
    #     return super().create(validated_data)
