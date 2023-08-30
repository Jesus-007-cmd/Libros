from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
#se importa authenticate 
from django.contrib.auth import authenticate, login #se importa authenticate y login
from django.contrib import messages
from django.contrib.auth import logout #se importa la de logout para mandar al modulo de logout del admin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserRegistrationForm


def custom_logout(request):
    logout(request) #se le pasa nuestro request que incluira toda la información para generar el logout
    return redirect('/login/') #redirect le especificamos a que url le vamos a redireccionar
# el logout ya casi esta listo lo unico es mandarle la petiión y presionar un boton, se busca la url 
#funcionalidad de custom login para hac
#El login sera en una función pero se puede cambiar a una clase
def custom_login(request): #kwards validacion de varios argumentos pero solo se accedera al puro metodo
    template_name='login.html'
    if request.method == 'POST':  #dos parametros se requieren para aceder al login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('--------------> Si entró al login')
            return redirect('/libros/inicio/')
        else:
            print('----------------> No entró al login')
            messages.error(request, 'Credenciales inválidas') 
    return render(request, template_name) #con render mandaremos dos paramtetros nuestra peticion y numero dos ahacia donde apuntara que es el templlate name
    # authentication y loginredirec url se crearan en el settings
    # AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
# LOGIN_REDIRECT_URL = '/libros/inicio'
  #   la primera es una confg que define en los backends authenticacino verificada por django
    # se configura para backend de configuracino proporcionado por django
# esto es para que el sistema en general sepa como se va a trabajar asi especificamos que reconozca users 
# como nuestro sistema de autenticacion general para lo que nosotros queramos mostrar
# y la segunda linea LOGIN_REIRECT... para especificar el login que debe que ir cuando nos 
# logeamos
# En el ejemplo la comentamos para ver como es que es necesaria 
# ahora nos vamos a template y crearemos el login.html
def index(request):

    return HttpResponse("Hola mundo")

def register(request):
    if request.method == 'POST': #Verificar si la solicitud de este tipo POST (envio de datos del formulario)    
       #Crear una instancia del formulario de registro  (con los datos enviados en la solicitud)
        form = UserRegistrationForm(request.POST)
        # Verificar si el formulario es valido (todos los campos requeridos están completos y las validaciones pasaron)
        if form.is_valid():
            #Guardar los datos del formulario en la base de datos (crear un nuevo usuario)
            form.save()
            #Obtener el nombre de usuario ingresando en el formulario
            username = form.cleaned_data.get('username')
            # Obtner la contraseña ingresada en el formulario (la contraseña ya está hasheada)
            password = form.cleaned_data.get('password1')
            # Autenticar al nuevo usuario recien registrado
            user = authenticate(username = username, password = password)
            # Iniciar sesión del usuario en la sesión actual
            login(request, user)
            # Redireccionar al usuario a la página de inicio (cambia 'home' por el nombre de la URL  que deseas redirigir)
            return redirect('inicio')
    else:
        # Si la solicitud no es de tipo POST, crear una isntancia de formulario en blanco
        form = UserRegistrationForm()
        # Renderizar la plantilla de registro con el formulario (ya sea en blanco o con datos ingresados previamente)
    return render(request, 'registration/register.html', {'form': form})

class Inicio(View):
    template_name = 'inicio.html'
    def post(self, request):

        return
    
    def get(self, request):
        '''
        Esta es mi clase get
        '''
        print('Ya inicio mi GET -------*')

        return render(request, self.template_name)
    