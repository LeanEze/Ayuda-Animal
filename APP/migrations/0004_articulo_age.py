# Generated by Django 4.0.5 on 2022-11-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_articulo_size_alter_articulo_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='age',
            field=models.CharField(choices=[('cachorro', 'Cachorro'), ('adulto', 'Adulto')], default='adulto', max_length=10),
        ),
    ]
