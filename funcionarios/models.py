from django.db import models

class Funcionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name="Nome do Funcionário")
    estado_civil = models.CharField(max_length=55, verbose_name="Estado Civil", blank=True, null=True)
    data_nasc = models.DateField(verbose_name="Data de Nascimento", blank=True, null=True)
    idade = models.IntegerField(verbose_name="Idade", blank=True, null=True)
    sexo = models.CharField(max_length=1, verbose_name="Sexo", blank=True, null=True)
    escolaridade = models.CharField(max_length=55, blank=True, null=True)
    ctps = models.CharField(max_length=30, blank=True, null=True)
    serie = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=18, unique=True, verbose_name="CPF")
    pis = models.CharField(max_length=40, blank=True, null=True)
    identidade = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    estado = models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=40, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    celular = models.CharField(max_length=18, blank=True, null=True)
    naturalidade = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField(max_length=55, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
