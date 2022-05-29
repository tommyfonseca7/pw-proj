from multiprocessing import context
from django.shortcuts import render
from .models import Post, Cadeira, Pessoa, Projeto, Interesse, Escola, Certificado, Competencia, Tecnologia, Noticia, Laboratorio, Site
from .forms import PostForm
from .models import PontuacaoQuizz
from django.http import HttpResponseRedirect
from django.urls import reverse
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.use("pgf")

def resolution_path(instance, filename):
    return f'users/{instance.id}/'

	
def home_page_view(request):
	return render(request, 'portfolio/home.html')

def licenciatura_page_view(request):
	context = { 'cadeiras' : Cadeira.objects.all(),
				'pessoas' : Pessoa.objects.all(),
				'projetos' : Projeto.objects.all(),
				'interesses' : Interesse.objects.all(),
				'escolas' : Escola.objects.all(),
				'certificados' : Certificado.objects.all(),
				'competencias' : Competencia.objects.all(),
				}
	return render(request, 'portfolio/licenciatura.html', context)

def projetos_page_view(request):
	context = { 'pessoas' : Pessoa.objects.all(),
				'projetos' : Projeto.objects.all()
				}
	return render(request, 'portfolio/projetos.html', context)

def web_page_view(request): 
	context={
		'tecnologias' : Tecnologia.objects.all(),
		'noticias' : Noticia.objects.all(),
		'sites' : Site.objects.all(),
		'laboratorios' : Laboratorio.objects.all()
	}
	return render(request, 'portfolio/web.html', context)		

def contact_page_view(request):
	return render(request, 'portfolio/contact.html')

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
		if request.POST['question-one'] == 'right':
			p+=20
		if request.POST['question-two'] == 'right':
			p+=20
		if request.POST['question-three'] == 'rapido':
			p+=20
		if request.POST['question-four'] == 'right':
			p+=20
		if request.POST['question-five'] == 'Python':
			p+=20
		return p
	

def desenha_grafico_resultados():
	persons = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.points, reverse=True)	
	nomes = []
	points = []
	for person in persons:
		nomes.append(person.name)
		points.append(person.points)
	plt.barh(nomes, points)
	plt.savefig('portfolio/static/portfolio/images/grafico.png', bbox_inches = 'tight')
	
def quizz(request):
		if request.method == 'POST':
			n = request.POST['name']
			p = pontuacao_quizz(request)
			r = PontuacaoQuizz(name=n, points=p)
			r.save()
		desenha_grafico_resultados()
		return render(request,'portfolio/web.html')		
	




