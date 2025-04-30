from django.shortcuts import render
from .models import *

def index(request):
    codigo = request.GET.get('codigo', '')

    certificado = Certificado.objects.filter(autenticacao=codigo).first()

    context = {
        'codigo': codigo,
        'certificado': certificado
    }

    return render(request, 'index.html', context)