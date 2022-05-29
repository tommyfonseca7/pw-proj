
from django import forms
from django.forms import ModelForm
from .models import Post, Projeto

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
