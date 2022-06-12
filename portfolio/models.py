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
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500, default='')
    imagem = models.ImageField(upload_to='projetos/')
    autores = models.ManyToManyField(Pessoa)
    ano = models.IntegerField(default=2020)
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    final = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo
    

class Cadeira(models.Model):
   nome = models.CharField(max_length=70)
   ano = models.IntegerField()
   semestre = models.IntegerField(default=1, validators=[MaxValueValidator(2), MinValueValidator(1)])
   etcs = models.IntegerField(default='6')
   descricao = models.TextField()
   rank = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
   ano_letivo = models.CharField(max_length=10, default='2020')
   professor = models.ManyToManyField(Pessoa)
   projetos = models.ManyToManyField(Projeto, blank=True)
   link = models.URLField(blank=True)
   def __str__(self):
       return self.nome

class Interesse(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='interesses/')
    
    def __str__ (self):
        return self.titulo

class Escola(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    ano_inicio = models.IntegerField(default=1)
    ano_fim = models.IntegerField(default=1)
    imagem = models.ImageField(upload_to='escolas/')

    def __str__ (self):
        return self.nome


class Certificado(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    ano = models.IntegerField(default=2020)
    link = models.FileField(default='', blank=True)

    def __str__ (self):
        return self.titulo

class Competencia(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=20)

    def __str__ (self):
        return self.titulo


class Tecnologia(models.Model):
    titulo = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    ano_criacao = models.IntegerField(default=1)
    criador = models.CharField(max_length=50)
    link = models.URLField(blank=True)
    descricao = models.CharField(max_length=500, blank=True)
    imagem = models.ImageField(upload_to='web/')

    def __str__ (self):
        return self.titulo

class Laboratorio(models.Model):
    titulo = models.CharField(max_length=60)
    descricao =  models.CharField(max_length=500, blank=True)
    link = models.URLField(blank=True)

    def __str__ (self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=60)
    descricao =  models.CharField(max_length=500, blank=True) 
    imagem = models.ImageField(upload_to='web/')
    date = models.DateField(blank=True)

    def __str__ (self):
        return self.titulo

class Site(models.Model):
    titulo = models.CharField(max_length=60)
    imagem = models.ImageField(upload_to='web/')
    link = models.URLField(blank=True)

    def __str__ (self):
        return self.titulo

