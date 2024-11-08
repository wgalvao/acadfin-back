from django.db import models


class CadServico(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
