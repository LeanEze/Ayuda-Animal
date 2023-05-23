# Generated by Django 4.0.6 on 2023-05-23 20:26

import ckeditor.fields
import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('social_network_one', models.URLField(null=True)),
                ('social_network_two', models.URLField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('short_content', models.CharField(max_length=180)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido')),
                ('content_upload', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen 1:')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen 2: ')),
                ('animal', models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otros', 'Otros')], default='Perro', max_length=8)),
                ('genero', models.CharField(choices=[('macho', 'Macho'), ('hembra', 'Hembra')], default='Macho', max_length=6)),
                ('size', models.CharField(choices=[('chico', 'Chico hasta 10kg'), ('mediano', 'Mediano entre 10kg/20kg'), ('grande', 'Grande +20kg')], default='chico', max_length=25, verbose_name='Tamaño')),
                ('age', models.CharField(choices=[('cachorro', 'Cachorro'), ('adulto', 'Adulto')], default='adulto', max_length=10, verbose_name='Edad')),
                ('is_headline', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='APP.publicador', verbose_name='Autor')),
            ],
        ),
    ]
