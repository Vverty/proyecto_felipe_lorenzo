"""
URL configuration for proyecto_felipe_lorenzo project.

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
from proyecto_felipe_lorenzo.views import saludo, segunda_vista, dia_de_hoy, mi_nombre_es, probandoTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('dia_de_hoy/', dia_de_hoy),
    path('mi_nombre_es/<nombre>', mi_nombre_es),
    path('probandoTemplate/', probandoTemplate)
]
