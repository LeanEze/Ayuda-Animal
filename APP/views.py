from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from APP.models import Articulo, Portal


def mostrar_inicio(request):
    return render(request, "APP/index.html", {})
    

def mostrar_adopcion(request):
    return render(request, "APP/Adopcion.html", {})


def mostrar_donaciones(request):
    return render(request, "APP/Donaciones.html", {})


def mostrar_contactenos(request):
    return render(request, "APP/Contactenos.html", {})

def mostrar_login(request):
    
    return render(request ,"APP_PANEL/panel_login.html", {})





class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Articulo.objects.filter(is_headline=True).order_by('date_updated').first()
        context['portal'] = Portal.objects.order_by('date_updated').first()
        return context    
