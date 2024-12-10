from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    desde = models.DateField()
    taxa_desconto = models.DecimalField(max_digits=18, decimal_places=2)
    limite_credito = models.DecimalField(max_digits=16, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return f"Cliente {self.nome}"
