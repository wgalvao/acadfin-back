from rest_framework import serializers
from .models import Funcao


class FuncaoSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.SerializerMethodField()

    class Meta:
        model = Funcao
        fields = ['id', 'nome', 'empresa', 'empresa_nome', 'codva', 'codvp',
                  'codvt', 'created_at', 'updated_at', 'user_id']

    def get_empresa_nome(self, obj):
        # Método que retorna o nome da empresa associada
        return obj.empresa.nome_razao if obj.empresa else None
