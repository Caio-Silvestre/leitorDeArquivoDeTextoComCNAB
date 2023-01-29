from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Handle_cnab(models.Model):
    type_operations = models.CharField(max_length=50)
    data = models.DateField()
    valor = models.DecimalField(max_digits=17, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.TextField(max_length=12)
    hora = models.TimeField()
    dono_da_loja = models.CharField(max_length=14)
    nome_da_loja = models.CharField(max_length=19)