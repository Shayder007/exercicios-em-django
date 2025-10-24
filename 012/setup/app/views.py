from django.http import HttpResponse

def produto(request, nome):
    nome = nome.replace('-', ' ').title()
    return HttpResponse(f"Produto solicitado: {nome}")
