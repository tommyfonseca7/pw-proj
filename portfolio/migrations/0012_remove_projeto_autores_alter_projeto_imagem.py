# Generated by Django 4.0.4 on 2022-05-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_projeto_ano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='autores',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(upload_to='projetos/'),
        ),
    ]
