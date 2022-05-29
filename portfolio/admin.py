from django.contrib import admin
from .models import Post, PontuacaoQuizz, Pessoa, Projeto, Cadeira, Interesse, Escola, Certificado, Competencia
from .models import Tecnologia, Noticia, Laboratorio, Site
# Register your models here.

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Cadeira)
admin.site.register(Interesse)
admin.site.register(Escola)
admin.site.register(Certificado)
admin.site.register(Competencia)
admin.site.register(Tecnologia)
admin.site.register(Noticia)
admin.site.register(Laboratorio)
admin.site.register(Site)