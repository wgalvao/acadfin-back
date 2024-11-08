from rest_framework import serializers
from .models import CadSindicato


class CadSindicatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadSindicato
        fields = ['id', 'nome', 'endereco',
                  'telefone', 'created_at', 'updated_at', 'user_id']

    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "O nome do sindicato deve ter pelo menos 3 caracteres.")
        return value
