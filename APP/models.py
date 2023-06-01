from django.db import models
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime   
from PIL import Image



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

ANIMAL_CHOICES = (
    ('perro','Perro'),
    ('gato', 'Gato'),
    ('otros', 'Otros')
)



class Articulo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    short_content = models.CharField(max_length=180)
    content = RichTextField(blank= True, null=True, verbose_name='Contenido')
    content_upload = RichTextUploadingField(blank= True, null=True)
    image = models.ImageField(upload_to="articles", null=True, blank=True, verbose_name='Imagen')
    image1 = models.ImageField(upload_to="articles", null=True, blank=True, verbose_name='Imagen 1:')
    image2 = models.ImageField(upload_to="articles", null=True, blank=True, verbose_name='Imagen 2: ')
    author = models.ForeignKey(Publicador, on_delete=models.DO_NOTHING, verbose_name='Autor')
    animal = models.CharField(max_length=8, choices=ANIMAL_CHOICES, default='Perro')
    genero = models.CharField(max_length=6, choices=GENERO_CHOICES, default='Macho')
    size = models.CharField(max_length=25, choices=SIZE_CHOICES, default='chico' ,verbose_name='Tamaño')
    age = models.CharField(max_length=10, choices=AGE_CHOICES, default='adulto', verbose_name='Edad')
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(default=datetime.now, verbose_name='Fecha')
    thumbnail = models.ImageField(upload_to='reduced', blank=True, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            img = Image.open(self.image.path)
            # Reducción de la imagen a un tamaño específico
            reduced_img = img.resize((300, 300))
            # Guardar la imagen reducida
            reduced_img.save(self.image.path.replace('articles', 'reduced'))
            # Asignar la ruta de la imagen reducida al campo correspondiente del modelo
            self.thumbnail = self.image.path.replace('articles', 'reduced')
            # Guardar el objeto actualizado en la base de datos
            super().save(*args, **kwargs)
        


class Portal(models.Model):
    name = models.CharField(max_length=20)
    social_network_one = models.URLField(null=True)
    social_network_two = models.URLField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
