from django.db import models
from django.contrib.auth.models import User


class Jornada(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.IntegerField()
    data_interacao = models.DateField()
    fase_jornada = models.CharField(max_length=25)
    acao = models.CharField(max_length=255)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)
    # user_id = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='jornadas')

    def __str__(self):
        return f"Jornada {self.id} - Cliente {self.cliente_id}"
