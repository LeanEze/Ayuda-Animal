# Generated by Django 4.0.6 on 2022-10-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='genero',
            field=models.CharField(choices=[(True, 'Macho'), (False, 'Hembra')], default='Macho', max_length=6),
        ),
    ]