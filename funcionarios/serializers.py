from rest_framework import serializers
from .models import Funcionario
import re

class FuncionarioSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.SerializerMethodField()
    cargo_nome = serializers.SerializerMethodField()  # Adicione este campo

    class Meta:
        model = Funcionario
        fields = '__all__'

    def validate_cpf(self, value):
        # Verifica se o CPF contém apenas números e tem 11 dígitos
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
            raise serializers.ValidationError("O CPF deve conter exatamente 11 dígitos numéricos.")

        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("O campo de email é obrigatório.")

        return value

    def get_empresa_nome(self, obj):
        return obj.empresa.nome_razao if obj.empresa else None

    def get_cargo_nome(self, obj):  # Adicione este método
        return obj.cargo.cargo if obj.cargo else None