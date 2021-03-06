# Generated by Django 4.0.4 on 2022-05-28 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_linguagem_pessoa_pontuacaoquizz_projeto_cadeira'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='ano_letivo',
            field=models.CharField(default='2020', max_length=10),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='etcs',
            field=models.IntegerField(default='6'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='rank',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='semestre',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='link_aluno',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='link_prof',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='linkedin',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='projeto',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(default='', upload_to='projetos/'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='youtube',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='autores',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
    ]
