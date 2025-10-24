from django.http import HttpResponse

def soma(request, a, b):
    return HttpResponse(f'A soma de {a} + {b} é {a + b}')