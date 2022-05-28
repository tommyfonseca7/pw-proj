from django.contrib import admin
from .models import Post
from .models import PontuacaoQuizz
from .models import Pessoa
from .models import Projeto
from .models import Cadeira

# Register your models here.

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Cadeira)