from django.shortcuts import HttpResponse
from django.utils.html import escape

def saudacao(request, nome):
    nome_seguro = escape(nome)
    return HttpResponse(f"Olá, {nome_seguro}!")

# Create your views here.
