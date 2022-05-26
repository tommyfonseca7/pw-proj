from multiprocessing import context
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home_page_view(request):
	return render(request, 'portfolio/home.html')

def licenciatura_page_view(request):
	return render(request, 'portfolio/licenciatura.html')

def projetos_page_view(request):
	return render(request, 'portfolio/projetos.html')		

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

