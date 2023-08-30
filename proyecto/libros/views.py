
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Libros
from .forms import LibroForm
from django.contrib import messages

from django.contrib.auth import logout #se importa la de logout para mandar al modulo de logout del admin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Sum, Max, Avg

#crear una función simple que me va a retornar el servidor
def index(request):

    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name = "index.html"
    @method_decorator(login_required)
    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        

        return render (request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def get(self, request):
        libros = Libros.objects.all()        
        form = LibroForm()        
        return render (request, self.template_name, {'form': form, 'libros': libros})

class Formulario(View):
    template_name = "formulario.html"
    @method_decorator(login_required)
    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        
        return render (request, self.template_name, {'form': form})
    @method_decorator(login_required)
    def get(self, request):
        libros = Libros.objects.all()
        form = LibroForm()
        return render (request, self.template_name, {'form': form, 'libros': libros})
    
class EliminarLibro(View):
    @method_decorator(login_required)
    def post(self, request, libro_id):
        libro = get_object_or_404(Libros, pk= libro_id)
        libro.delete()
        return redirect('inicio')
    
def estadisticas_libros(request):
    #Obtener el número total de páginas de todos los libros
    total_paginas = Libros.objects.aggregate(total_paginas=Sum('paginas'))['total_paginas']

    #Obtener el año máximo de pulicación
    max_anio_publicacion = Libros.objects.aggregate(max_anio_publicacion=Max('año_publicacion'))['max_anio_publicacion']

    #Obtener el número promedio de paginas de todos los libros 
    promedio_paginas = Libros.objects.aggregate(promedio_paginas=Avg('paginas'))['promedio_paginas']
    return render(request, 'estadisticas/estadisticas_libros.html',
    { 'total_paginas':total_paginas,
     'max_anio_publicacion': max_anio_publicacion,
      'promedio_paginas': promedio_paginas })

#def insertar_libro(request):
 #   nuevo_libro = Libros(
        ##titulo="El gran libro",
        #edicion="Primera edición",
        #editorial="XYZ",
        #año_publicacion=2022,
        #paginas=200
    #)
    #nuevo_libro.save()

#0    return HttpResponse("Libro insertado correctamente") 

