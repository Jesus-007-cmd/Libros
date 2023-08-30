from typing import Any, Dict
from django import forms
from .models import Libros

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo','edicion', 'editorial','año_publicacion','paginas']
    #Este metodo clean permitira validar que los campos tengan todos los datos en caso de que nos
    #  mandara mensaje: rellena este campo
    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo') #que empate o tenga los atributos en mi modelo titulo
        edicion = cleaned_data.get('edicion')
        editorial = cleaned_data.get('editorial')
        año_publicacion = cleaned_data.get('año_publicacion')
        paginas = cleaned_data.get('paginas')

        #validaremos que no tenga valor ninguno de estos campos:
        if not titulo or not edicion or not editorial or not año_publicacion or not paginas:
            #se gnera una excpecion directamente con el metodo raise:
             # este genera una exceepcion y retrona un json response al html con el mensaje que se ponga
            raise forms.ValidationError("Todos los campos deben estar completos") #este mensaje se mandara como un log
        return cleaned_data #regrsa el cleaned_data el cual ya se encargo todo el proceso
    
