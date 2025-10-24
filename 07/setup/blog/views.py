from django.http import HttpResponse

def artigo(request, slug):
    titulo = slug.replace('-', ' ').replace('_', ' ').title()
    return HttpResponse(f"Artigo solicitado: {titulo}")
