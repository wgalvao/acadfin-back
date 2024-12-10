from django.db import models
from clientes.models import Cliente


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    # nome_razao = models.CharField(max_length=255)  # Mantido obrigatório
    nome_razao = models.CharField(
        max_length=255, blank=True, null=True)  # Mantido obrigatório
    # cnpj = models.CharField(max_length=55, unique=True)  # Mantido obrigatório
    cnpj = models.CharField(max_length=55, blank=True,
                            null=True)  # Mantido obrigatório
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=80, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=80, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    telefone = models.CharField(max_length=18, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    preposta = models.CharField(max_length=250, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return f"{self.nome_razao} ({self.cnpj})"
