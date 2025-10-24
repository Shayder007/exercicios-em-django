from django.http import HttpResponse, HttpResponseBadRequest
import re

EMAIL_RE = re.compile(r'^[\w\.\-]+@[\w\.\-]+\.\w{2,}$')

def email(request, email):
    if EMAIL_RE.match(email):
        return HttpResponse(f"E-mail válido: {email}")
    return HttpResponseBadRequest("Email inválido")
