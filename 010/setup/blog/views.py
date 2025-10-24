from django.http import HttpResponse

# Simulando um banco de dados (dicionário)
POSTS = [
    {"titulo": "Primeiro Post", "slug": "primeiro-post", "ano": 2025, "autor": "shayder"},
    {"titulo": "Aprendendo Django", "slug": "aprendendo-django", "ano": 2025, "autor": "maria"},
    {"titulo": "BitDogLab é braba", "slug": "bitdoglab-e-braba", "ano": 2024, "autor": "shayder"},
]

def index(request):
    lista = "<br>".join([f"{p['ano']} — {p['titulo']}" for p in POSTS])
    return HttpResponse(f"📚 Lista de posts:<br>{lista}")

def post(request, ano, slug):
    for p in POSTS:
        if p["ano"] == ano and p["slug"] == slug:
            return HttpResponse(f"📰 {p['titulo']} — ({p['ano']})<br>Autor: {p['autor'].title()}")
    return HttpResponse("Post não encontrado!", status=404)

def autor(request, nome):
    filtrados = [p for p in POSTS if p["autor"].lower() == nome.lower()]
    if not filtrados:
        return HttpResponse(f"Nenhum post do autor: {nome}", status=404)

    lista = "<br>".join([f"{p['ano']} — {p['titulo']}" for p in filtrados])
    return HttpResponse(f"Posts de {nome.title()}:<br>{lista}")
