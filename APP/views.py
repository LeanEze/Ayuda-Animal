from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from APP.models import Articulo, Portal

#Muestra template inicio

def mostrar_inicio(request):
    return render(request, "APP/index.html", {})
    
#Muestra template adopcion
def mostrar_adopcion(request):
    return render(request, "APP/Adopcion.html", {})

#Muestra template donaciones
def mostrar_donaciones(request):
    return render(request, "APP/Donaciones.html", {})

#Muestra template contactenos
def mostrar_contactenos(request):
    return render(request, "APP/Contactenos.html", {})

#Muestra template transito
def mostrar_transito(request):
    return render(request, "APP/Transito.html", {})

#Muestra template inicio de sesion
def mostrar_login(request):
    
    return render(request ,"APP_PANEL/panel_login.html", {})



# Estos le permiten estructurar sus vistas y reutilizar el código aprovechando la herencia y los mixins.
class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Articulo.objects.filter(is_headline=True).order_by('date_updated').first()
        context['portal'] = Portal.objects.order_by('date_updated').first()
        return context    
