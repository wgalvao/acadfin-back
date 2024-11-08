from rest_framework import serializers
from .models import Funcionario
import re

class FuncionarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Funcionario
        fields = '__all__'
    
    def validate_cpf(self, value):
        # Verifica se o CPF contém apenas números e tem 11 dígitos
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
            raise serializers.ValidationError("O CPF deve conter exatamente 11 dígitos numéricos.")
        
        # Verifica se o CPF é válido com base em um algoritmo simples de validação
        # if not self.validar_cpf(value):
        #     raise serializers.ValidationError("CPF inválido.")
        
        return value

    def validate_email(self, value):
        # Django já realiza validação básica de email, mas podemos adicionar regras adicionais se necessário.
        if not value:
            raise serializers.ValidationError("O campo de email é obrigatório.")
        
        return value
    
    def validar_cpf(self, cpf):
        # Implementa um algoritmo de validação para CPF (digitos verificadores)
        cpf = [int(char) for char in cpf]
        
        # Calcula o primeiro dígito verificador
        for i in range(9, 11):
            val = sum((cpf[num] * ((i + 1) - num) for num in range(0, i))) % 11
            if val >= 10:
                val = 0
            if val != cpf[i]:
                return False
        return True
