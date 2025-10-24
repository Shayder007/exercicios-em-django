from django.http import FileResponse, Http404, HttpResponse
import os

# Caminho da pasta onde ficarão os arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

def download(request, nome, ext):
    # Extensões permitidas (controle de segurança!)
    allowed_ext = {'pdf', 'txt', 'jpg', 'png'}
    
    if ext not in allowed_ext:
        return HttpResponse("Extensão não permitida!", status=400)

    file_path = os.path.join(MEDIA_DIR, f"{nome}.{ext}")

    if not os.path.exists(file_path):
        raise Http404("Arquivo não encontrado!")

    return FileResponse(open(file_path, 'rb'), as_attachment=True)
