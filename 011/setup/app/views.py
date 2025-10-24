from django.http import HttpResponse

def mostra_numero(request, num):
    return HttpResponse(f"Você digitou o número: {num}")
