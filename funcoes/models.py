from django.db import models

from empresas.models import Empresa


class Funcao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE)
    codva = models.IntegerField()
    codvp = models.IntegerField()
    codvt = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
