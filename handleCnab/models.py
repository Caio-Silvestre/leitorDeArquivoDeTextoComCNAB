from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class HandleCnab(models.Model):
    typeOperations = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(9)])
    data = models.DateTimeField()
    valor = models.FloatField()
    cpf = models.IntegerField()
    cartao = models.IntegerField()
    hora = models.TimeField()
    donoDaLoja = models.CharField(max_length=200)
    nomeDaLoja = models.CharField(max_length=200)