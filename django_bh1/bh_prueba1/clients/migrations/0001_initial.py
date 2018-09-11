# Generated by Django 2.0.2 on 2018-09-02 22:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('address', ckeditor.fields.RichTextField(verbose_name='Dirección')),
                ('second_adress', ckeditor.fields.RichTextField(verbose_name='Segunda Dirección')),
                ('city', models.CharField(max_length=200, verbose_name='Ciudad')),
                ('rfc', models.CharField(max_length=13, verbose_name='RFC')),
                ('phone', models.CharField(max_length=24, verbose_name='Teléfono')),
                ('mobile', models.CharField(max_length=24, verbose_name='Teléfono Móvil')),
                ('email', models.CharField(max_length=200, verbose_name='Correo Electrónico')),
                ('website', models.CharField(max_length=200, verbose_name='Página Web')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'ordering': ['created', 'name'],
            },
        ),
    ]