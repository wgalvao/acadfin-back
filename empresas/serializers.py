# empresas/serializers.py
from rest_framework import serializers
from .models import Empresa
import re


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id', 'nome_razao', 'cnpj', 'endereco', 'numero', 'nome_fantasia', 'inscricao_estadual',
            'bairro', 'cidade', 'estado', 'cep', 'telefone', 'email', 'preposta', 'user_id',
            'created_at', 'updated_at'
        ]

    # def validate_cnpj(self, value):
    #     if not re.match(r'^\d{14}$', value):
    #         raise serializers.ValidationError("O CNPJ deve ter 14 dígitos numéricos.")
    #     return value

    # def validate_email(self, value):
    #     if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
    #         raise serializers.ValidationError("O e-mail não é válido.")
    #     return value
