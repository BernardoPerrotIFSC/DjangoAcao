from django.shortcuts import render, redirect
from .models import Acao
from .forms import CreateAcao
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import yfinance as yf


# Create your views here.

def home(request):
    return render(request, "main/home.html")

def acao(request):
    # return render(request, "main/acao.html")
    if request.method == 'POST':
        form = CreateAcao()
        if form.is_valid():
            codigo = form.cleaned_data['ticker']
            ticker = yf.Ticker( codigo+".SA" )
            preco_pago = form.cleaned_data['preco_paga']
            quantidade = form.cleaned_data['quantidade']
            data_compra = form.cleaned_data['data_compra']
            valor_pago = round(preco_pago*quantidade, 2)
            preco_atual = round(acao.history(period='1d')['Close'][0], 2)
            valor_atual = round(preco_atual*quantidade, 2)
            lucro_prejuizo = round(valor_atual-valor_pago, 2)
            rentabilidade = round(lucro_prejuizo/valor_pago*100, 2)
            user = request.user.id
            acao = Acao(user=user, ticker=ticker, preco_pago=preco_pago, quantidade=quantidade, data_compra=data_compra, valor_pago=valor_pago, preco_atual=preco_atual, valor_atual=valor_atual, lucro_prejuizo=lucro_prejuizo, rentabilidade=rentabilidade)
            acao.save()
            messages.success(request, "Ação adicionada a carteira!")
        else:
            form = CreateAcao()
        return redirect("/acao")
    return render(request, "main/acao.html", {"form":form})
    
            



