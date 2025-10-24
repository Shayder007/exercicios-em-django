from django.http import HttpResponse
from django.utils.html import escape

def perfil(request, nome=None):
    if nome:
        return HttpResponse(f"Perfil de {escape(nome)}")
    return HttpResponse("Perfil de visitante")