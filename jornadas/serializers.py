from rest_framework import serializers
from .models import Jornada


class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = ['id', 'cliente_id', 'data_interacao', 'fase_jornada',
                  'acao', 'feedback', 'created_at', 'updated_at', 'user_id']
