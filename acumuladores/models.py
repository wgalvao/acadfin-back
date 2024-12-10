from django.db import models
from django.contrib.auth.models import User


class Acumulador(models.Model):
    id = models.AutoField(primary_key=True)
    acumulador = models.CharField(max_length=255)
    tipo = models.CharField(max_length=55)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acumuladores')
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.acumulador
