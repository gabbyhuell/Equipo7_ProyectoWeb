# Generated by Django 4.0.6 on 2022-12-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20221211_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, null=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_eliminacion',
            field=models.DateField(auto_now=True, null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(max_length=511, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, null=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='redessociales',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=50, verbose_name='Usuario registrado'),
        ),
        migrations.AlterField(
            model_name='web',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='web',
            name='telefono',
            field=models.CharField(max_length=13, verbose_name='Teléfono'),
        ),
    ]
