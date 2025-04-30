from django.contrib import admin
from .models import Certificado

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'cpf', 'autenticacao', 'carga_horaria', 'periodo_de_tempo')
    search_fields = ('nome', 'cpf', 'curso')
    list_filter = ('curso', 'periodo_de_tempo')
