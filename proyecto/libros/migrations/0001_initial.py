# Generated by Django 4.2.2 on 2023-06-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cafe', models.CharField(default='sin nombrar', max_length=300, verbose_name='Tipo de Cafe')),
                ('contenido', models.IntegerField(verbose_name='Contenido')),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='sin titulo', max_length=300, verbose_name='Titulo')),
                ('edicion', models.CharField(default='sin especificar', max_length=300, verbose_name='Edicion')),
                ('editorial', models.CharField(default='sin especificar', max_length=300, verbose_name='Editorial')),
                ('año_pub', models.IntegerField(default=0, verbose_name='Año de Publicación')),
                ('pagina', models.IntegerField(default='no aplica', verbose_name='Pagina')),
            ],
        ),
    ]