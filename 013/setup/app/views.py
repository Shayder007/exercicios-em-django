from django.http import HttpResponse

def usuario(request, nome, idade):
    return HttpResponse(f"Usuário: {nome.title()} — Idade: {idade}")