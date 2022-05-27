from multiprocessing import context
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from .models import PontuacaoQuizz
from django.http import HttpResponseRedirect
from django.urls import reverse


def home_page_view(request):
	return render(request, 'portfolio/home.html')

def licenciatura_page_view(request):
	return render(request, 'portfolio/licenciatura.html')

def projetos_page_view(request):
	return render(request, 'portfolio/projetos.html')

def web_page_view(request):
	return render(request, 'portfolio/web.html')		

def blog_page_view(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'portfolio/blog.html', context)

def newpost_page_view(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:blog'))
	
	context = {'form' : form}

	return render(request, 'portfolio/newpost.html', context)

def	editpost_page_view(request, post_id):
	post = Post.objects.get(id = post_id)
	form = PostForm(request.POST or None, instance=post)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:blog'))
	
	context = {'form' : form, 'post_id': post_id}
	return render(request, 'portfolio/editpost.html', context)

def deletepost_view_page(request,post_id):
	Post.objects.get(id=post_id).delete()
	return HttpResponseRedirect(reverse('portfolio:blog'))

def pontuacao_quizz(request):
	p = 0
	if request.method == 'POST':
		if request.POST['question-one'] == 'Front-End':
			p+=1
		if request.POST['question-two'] == 'certo':
			p+=1
		if request.POST['question-three'] == 'certo':
			p+=1
		if request.POST['question-four'] == 'rapido':
			p+=1
		if request.POST['question-five'] == 'Python':
			p+=1
		return p
	


def quizz(request):
   if request.method == 'POST':
      n = request.POST['name']
      p = pontuacao_quizz(request)
      r = PontuacaoQuizz(nome=n, pontuacao=p)
      r.save()

def desenha_grafico_resultados():
	persons = PontuacaoQuizz.objects.all()
	persons.sorted(persons.points)
	for person in persons:
		names = names.append(person.name)
		points = points.append(person.points)	
	




