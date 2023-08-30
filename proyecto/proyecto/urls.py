from . import views
from django.contrib import admin
from django.urls import path, include

#importaciones se requiere de views un metodo que facilita el login con el login del admin
#Se importa archivo views pero se importara con nombre distinto para no hacer redundancia con el views pasado
from django.contrib.auth import views as auth_views
#como buena practica las importaciones se saltean de 3 en 3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include("libros.urls")),
    #se importa loginviews y como es una clase se hace como as view, como no se 
    # tiene acceso directamente al view se le va a mandar como parametro template_name 
    # para que lo pueda utilizar y nos redirija hacia el template que queremos pasarle
    #login.html lo vamos a crear dentro de templates
    path('login/', views.custom_login ,name='login' ),
    path('logout/', views.custom_logout, name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register , name='register'),   
]
