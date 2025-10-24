from django.http import HttpResponse

def produto(request, categoria, produto):
    # Organiza os textos para ficarem bonitos
    categoria = categoria.replace('-', ' ').title()
    produto = produto.replace('-', ' ').title()

    return HttpResponse(f"Categoria: {categoria} — Produto: {produto}")