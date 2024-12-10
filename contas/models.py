from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    id = models.AutoField(primary_key=True)
    conta = models.CharField(max_length=255)
    tipo_conta = models.CharField(max_length=55)
    descricao = models.TextField(null=True, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(null=True, blank=True)
    # user_id = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='contas')

    def __str__(self):
        return self.conta
