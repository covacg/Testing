"""
URL configuration for mechanicsrevolution project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #URLS HOME
    path('', views.home_login, name='principal'),
    path('registeroption',views.register_option, name='registeroption'),
    path('taller',views.taller,name='taller'),
    path('cliente',views.cliente, name='cliente'),
    

    #URLS CLIENTES
    path('calendario', views.clientes_calendario, name='ccalendario'),
    path('talleres',views.clientes_talleres, name='ctalleres'),
    path('vehiculos',views.clientes_vehiculos, name='cvehiculos'),
    path('notificaciones',views.clientes_notificacion, name='cnotificaciones'),
    path('edit',views.clientes_edit, name='cperfil'),

    #URLS TALLERES
    path('analitica', views.talleres_analitica, name='tanalitica'),
    path('citas',views.talleres_citas, name='tcalendario'),
    path('servicios',views.talleres_servicios, name='tservicios'),
    path('notificacion',views.talleres_notificacion, name='tnotificaciones'),
    path('perfil',views.talleres_edit, name='tperfil')
]