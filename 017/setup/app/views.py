from django.http import HttpResponse

def artigo(request, slug):
    titulo = slug.replace('-', ' ').title()
    return HttpResponse(f"Artigo: {titulo}")
