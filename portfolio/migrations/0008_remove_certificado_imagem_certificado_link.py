# Generated by Django 4.0.4 on 2022-05-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_certificados_certificado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificado',
            name='imagem',
        ),
        migrations.AddField(
            model_name='certificado',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
