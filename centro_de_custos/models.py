from django.db import models


class CadCentroDeCustos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    codigo = models.CharField(max_length=55)
    ativo = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
