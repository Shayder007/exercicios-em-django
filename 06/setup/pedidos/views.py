from django.http import HttpResponse

def index(request):
    return HttpResponse("Lista de pedidos")

def detalhes(request, id):
    return HttpResponse(f"Detalhes do pedido ID: {id}")