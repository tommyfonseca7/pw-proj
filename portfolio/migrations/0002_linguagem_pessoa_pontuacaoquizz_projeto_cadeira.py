# Generated by Django 4.0.4 on 2022-05-28 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiulo', models.CharField(max_length=30)),
                ('autores', models.ManyToManyField(related_name='projeto', to='portfolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('ano', models.IntegerField()),
                ('descricao', models.TextField()),
                ('docente_teorica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
                ('docentes_praticas', models.ManyToManyField(related_name='caderias', to='portfolio.pessoa')),
                ('linguagens', models.ManyToManyField(to='portfolio.linguagem')),
                ('projetos', models.ManyToManyField(to='portfolio.projeto')),
            ],
        ),
    ]