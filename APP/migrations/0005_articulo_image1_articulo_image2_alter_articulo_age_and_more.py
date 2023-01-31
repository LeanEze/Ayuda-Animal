# Generated by Django 4.0.6 on 2023-01-31 19:47

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_articulo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen 1:'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen 2: '),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='age',
            field=models.CharField(choices=[('cachorro', 'Cachorro'), ('adulto', 'Adulto')], default='adulto', max_length=10, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='APP.publicador', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='size',
            field=models.CharField(choices=[('chico', 'Chico hasta 10kg'), ('mediano', 'Mediano entre 10kg/20kg'), ('grande', 'Grande +20kg')], default='chico', max_length=25, verbose_name='Tamaño'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]