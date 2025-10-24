from django.http import HttpResponse, HttpResponseBadRequest
from datetime import datetime

def agenda(request, data):
    try:
        dt = datetime.strptime(data, '%Y-%m-%d').date()
        return HttpResponse(f"Data válida: {dt}")
    except:
        return HttpResponseBadRequest("Data inválida")
