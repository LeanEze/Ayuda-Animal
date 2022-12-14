from django.db import models
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime   



class Publicador(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"


GENERO_CHOICES = (
    ('macho','Macho'),
    ('hembra', 'Hembra'),
)

SIZE_CHOICES = (
    ('chico','Chico hasta 10kg'),
    ('mediano', 'Mediano entre 10kg/20kg'),
    ('grande', 'Grande +20kg')
)

AGE_CHOICES = (
    ('cachorro','Cachorro'),
    ('adulto', 'Adulto')
)


class Articulo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    short_content = models.CharField(max_length=180)
    content = RichTextField(blank= True, null=True, verbose_name='Contenido')
    content_upload = RichTextUploadingField(blank= True, null=True)
    image = models.ImageField(upload_to="articles", null=True, blank=True, verbose_name='Imagen')
    author = models.ForeignKey(Publicador, on_delete=models.DO_NOTHING, verbose_name='Autor')
    genero = models.CharField(max_length=6, choices=GENERO_CHOICES, default='Macho')
    size = models.CharField(max_length=25, choices=SIZE_CHOICES, default='chico' ,verbose_name='Tamaño')
    age = models.CharField(max_length=10, choices=AGE_CHOICES, default='adulto', verbose_name='Edad')
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(default=datetime.now, verbose_name='Fecha')



class Portal(models.Model):
    name = models.CharField(max_length=20)
    social_network_one = models.URLField(null=True)
    social_network_two = models.URLField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
