from unicodedata import name
from django.db import models
from django import forms

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateField(help_text="Formato da Data : YYYY/MM/DD")
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    header_image = models.ImageField(null = True, blank= True, upload_to="static\posts\images")
    
    def __str__(self):
        return self.titulo[:20]


class PontuacaoQuizz(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
