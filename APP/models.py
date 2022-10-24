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

class Articulo(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=180)
    content = RichTextField(blank= True, null=True)
    content_upload = RichTextUploadingField(blank= True, null=True)
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    author = models.ForeignKey(Publicador, on_delete=models.DO_NOTHING)
    genero = models.CharField(max_length=6, choices=GENERO_CHOICES, default='Macho')
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(default=datetime.now)


class Portal(models.Model):
    name = models.CharField(max_length=20)
    social_network_one = models.URLField(null=True)
    social_network_two = models.URLField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
