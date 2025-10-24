from django.http import HttpResponse

def arquivo(request, nome, ext):
    return HttpResponse(f"Arquivo: {nome}.{ext}")
