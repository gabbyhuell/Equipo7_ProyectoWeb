# Generated by Django 4.0.6 on 2022-12-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_noticia_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(max_length=511, verbose_name='Contenido'),
        ),
    ]
