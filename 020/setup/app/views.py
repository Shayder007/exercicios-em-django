from django.http import HttpResponse, HttpResponseBadRequest

def lista_posts(request):
    return HttpResponse("Lista de posts ")

def post(request, ano, mes, slug):
    ano = int(ano)
    mes = int(mes)

    if not (1 <= mes <= 12):
        return HttpResponseBadRequest("Mês inválido")

    return HttpResponse(
        f"Post: {slug.replace('-',' ').title()} — {mes}/{ano}"
    )
