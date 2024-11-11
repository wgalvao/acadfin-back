from django.db import models


class Funcao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    empresa = models.IntegerField()
    codva = models.IntegerField()
    codvp = models.IntegerField()
    codvt = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
