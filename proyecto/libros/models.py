from django.db import models


class Libros(models.Model):
    class Meta:
            verbose_name="Libro"
            verbose_name_plural="Libros"
    titulo = models.CharField("Título", max_length=300, default="Sin nombrar")
    edicion = models.CharField("Edición", max_length=300, default="Sin especificar")
    editorial = models.CharField("Editorial", max_length=300, default="sin especificar")
    año_publicacion = models.IntegerField("Año de publicación",  default=0)
    paginas = models.IntegerField("Número de páginas",  blank=False)

    def _str_(self):
            return self.titulo