# funcionarios/serializers.py

from rest_framework import serializers
from .models import Funcionario
from cargos.models import Cargo  # Importe o modelo Cargo


class FuncionarioSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.SerializerMethodField()
    cargo_nome = serializers.SerializerMethodField()
    salario = serializers.SerializerMethodField()  # Novo campo para o salário

    class Meta:
        model = Funcionario
        fields = '__all__'

    def get_empresa_nome(self, obj):
        return obj.empresa.nome_razao if obj.empresa else None

    def get_cargo_nome(self, obj):
        return obj.cargo.cargo if obj.cargo else None

    def get_salario(self, obj):  # Método para obter o salário do cargo
        if obj.cargo:
            cargo = Cargo.objects.get(id=obj.cargo.id)
            return cargo.salario
        return None
