# Generated by Django 4.1.3 on 2022-12-21 18:18

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
