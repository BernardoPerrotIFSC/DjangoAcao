from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Acao(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    codigo = models.CharField(max_length=10)
    preco_pago = models.FloatField()
    valor_pago = models.FloatField()
    quantidade = models.IntegerField()
    data_compra = models.DateField()
    preco_atual = models.FloatField()
    valor_atual = models.FloatField()
    lucro_prejuizo = models.FloatField()
    rentabilidade = models.FloatField()
