from rest_framework import serializers
from .models import Cargo


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'cargo', 'descricao', 'nivel',
                  'salario', 'ativo', 'created_at', 'updated_at', 'user_id']

    def validate_salario_base(self, value):
        """
        Validate if salary is positive
        """
        if value < 0:
            raise serializers.ValidationError(
                "Salário base não pode ser negativo")
        return value

    # def validate_nome(self, value):
    #     """
    #     Validate if the cargo name is unique (case insensitive)
    #     """
    #     # Check if there's another cargo with the same name (case insensitive)
    #     if Cargo.objects.filter(nome__iexact=value).exists():
    #         if self.instance and self.instance.nome.lower() == value.lower():
    #             return value
    #         raise serializers.ValidationError(
    #             "Já existe um cargo com este nome")
    #     return value
