from unicodedata import name
from . import views
from django.urls import path


app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('newpost', views.newpost_page_view, name='newpost'),
    path('editpost/<int:post_id>', views.editpost_page_view, name='editpost'),
    path('deletepost/<int:post_id>', views.deletepost_view_page, name='deletepost'),
    path('web', views.web_page_view, name='web'),
    path('contact', views.contact_page_view, name='contact'),
    path('quizz', views.quizz, name='quizz'),
    path('newproj', views.new_project_view, name='newproj'),
    path('editproj/<int:projeto_id>', views.edit_project_view,name='editproj'),
    path('deleteproj/<int:projeto_id>', views.delete_project_view,name='deleteproj'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('contact', views.contact_page_view, name='contact'),


]