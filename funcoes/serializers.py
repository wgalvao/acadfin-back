from rest_framework import serializers
from .models import Funcao


class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = ['id', 'nome', 'empresa', 'codva', 'codvp',
                  'codvt', 'created_at', 'updated_at', 'user_id']
