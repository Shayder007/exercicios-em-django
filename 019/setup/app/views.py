from django.http import HttpResponseRedirect, HttpResponseBadRequest

ALLOWED = {"exemplo.com", "teste.org"}

def site(request, dominio):
    if dominio not in ALLOWED:
        return HttpResponseBadRequest("Domínio não permitido")
    return HttpResponseRedirect(f"https://{dominio}")
