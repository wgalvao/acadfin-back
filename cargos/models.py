from django.db import models


class Cargo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cargo = models.CharField(max_length=255)
    descricao = models.TextField()
    nivel = models.CharField(max_length=55)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.cargo
