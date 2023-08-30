# Generated by Django 4.2.2 on 2023-06-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libros',
            name='año_pub',
        ),
        migrations.RemoveField(
            model_name='libros',
            name='pagina',
        ),
        migrations.AddField(
            model_name='libros',
            name='año_publicacion',
            field=models.IntegerField(default=200, verbose_name='Año de publicación'),
        ),
        migrations.AddField(
            model_name='libros',
            name='paginas',
            field=models.IntegerField(default=200, verbose_name='Número de páginas'),
        ),
        migrations.AlterField(
            model_name='libros',
            name='edicion',
            field=models.CharField(default='Sin especificar', max_length=300, verbose_name='Edición'),
        ),
        migrations.AlterField(
            model_name='libros',
            name='titulo',
            field=models.CharField(default='Sin nombrar', max_length=300, verbose_name='Título'),
        ),
    ]
