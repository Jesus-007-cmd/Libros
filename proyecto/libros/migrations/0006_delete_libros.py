# Generated by Django 4.2.2 on 2023-06-14 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_alter_libros_paginas'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Libros',
        ),
    ]