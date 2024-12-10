from django.db import models
from django.contrib.auth.models import User


class Aliquota(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_imposto = models.CharField(max_length=55)
    percentual = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.CharField(max_length=55)
    descricao = models.TextField(null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(null=True, blank=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aliquotas')

    def __str__(self):
        return f"{self.tipo_imposto} - {self.estado}"
