from django.db import models
from django.contrib.auth.models import User


class BaseCalculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo = models.CharField(max_length=55)
    percentual = models.DecimalField(max_digits=5, decimal_places=2)
    valor_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)
    # user_id = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='base_calculos')

    def __str__(self):
        return self.nome
