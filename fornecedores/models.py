from django.db import models
from django.contrib.auth.models import User


class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa_id = models.IntegerField()
    desde = models.DateField()
    observacao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fornecedores')

    def __str__(self):
        return f"Fornecedor {self.id}"
