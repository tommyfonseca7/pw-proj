# Generated by Django 4.0.4 on 2022-05-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_remove_projeto_autores_alter_projeto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='autores',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
    ]
