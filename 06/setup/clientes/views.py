from django.http import HttpResponse

def index(request):
    return HttpResponse("Lista de clientes ")

def detalhes(request, id):
    return HttpResponse(f"Detalhes do cliente ID: {id}")