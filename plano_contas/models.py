from django.db import models
from django.contrib.auth.models import User


class PlanoContas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_contas = models.CharField(max_length=40)
    nome_conta = models.CharField(max_length=255)
    tipo_conta = models.CharField(max_length=55)
    nivel = models.CharField(max_length=55)
    descricao = models.TextField(blank=True, null=True)
    conta_pai = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plano_contas')

    def __str__(self):
        return self.nome_conta
