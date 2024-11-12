from django.db import models
from django.contrib.auth.models import User


class Cfop(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    tipo_operacao = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cfops')
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.codigo
