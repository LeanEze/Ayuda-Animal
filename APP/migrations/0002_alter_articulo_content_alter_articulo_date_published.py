# Generated by Django 4.0.6 on 2022-10-17 23:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='date_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
