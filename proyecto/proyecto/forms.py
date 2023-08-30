from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    #Agregar un campo adicional para el correo electrónico (EmailField)
    email = forms.EmailField

    class Meta:
        #Especificar el modelo con el que está relacionado el formulario
        model = User
        # Especificar los campos que se mostrarán en el formulario (User en este caso)
        fields = ['username','email', 'password1','password2']
    