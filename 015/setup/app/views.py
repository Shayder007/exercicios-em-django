from django.http import HttpResponse

def perfil(request, nome=None):
    if nome:
        return HttpResponse(f"Perfil de {nome.title()}")
    return HttpResponse("Perfil de visitante")