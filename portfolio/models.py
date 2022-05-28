from distutils.command.upload import upload
from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateField(help_text="Formato da Data : YYYY/MM/DD")
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    link = models.URLField(default='')
    
    def __str__(self):
        return self.titulo[:20]


class PontuacaoQuizz(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()

class Linguagem(models.Model):
    nome = models.CharField(max_length=20)

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.URLField(default='')
    link_prof = models.URLField(blank=True)
    link_aluno = models.URLField(blank=True)

    def __str__(self):
        if self.link_aluno == "":
            return "Professor " + self.nome
        else:
            return "Aluno " + self.nome

class Projeto(models.Model):
    tiulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500, default='')
    imagem = models.ImageField(upload_to='projetos/', default = '')
    autores = models.ManyToManyField(Pessoa)
    ano = models.IntegerField
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
    

class Cadeira(models.Model):
   nome = models.CharField(max_length=50)
   ano = models.IntegerField()
   semestre = models.IntegerField(default=1, validators=[MaxValueValidator(2), MinValueValidator(1)])
   etcs = models.IntegerField(default='6')
   descricao = models.TextField()
   rank = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
   ano_letivo = models.CharField(max_length=10, default='2020')
   docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
   projetos = models.ManyToManyField(Projeto, blank=True)
   link = models.URLField(blank=True)
   def __str__(self):
       return self.nome



