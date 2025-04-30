from django.db import models

class Certificado(models.Model):
    autenticacao = models.CharField(max_length=500, unique=True, null=False)
    curso = models.CharField(max_length=500, null=False)
    nome = models.CharField(max_length=500, null=False)
    cpf = models.CharField(max_length=500, null=False)
    carga_horaria = models.CharField(max_length=500, null=False)
    periodo_de_tempo = models.CharField(max_length=500, null=False)

    def __str__(self):
        return f"Certificado de {self.nome} - {self.curso}"
