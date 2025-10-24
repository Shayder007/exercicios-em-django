from django.shortcuts import HttpResponse

def boas_vindas(request):
    return HttpResponse("Seja bem-vindo ao Django!")