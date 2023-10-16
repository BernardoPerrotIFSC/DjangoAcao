from django import forms
from .models import Acao

class CreateAcao(forms.Form):
    ticker = forms.CharField(label="Código", max_length=10)
    preco_pago = forms.FloatField(label="Preço Pago")
    quantidade = forms.IntegerField(label="Quantidade")
    data_compra = forms.DateField(label="Data Compra")


    