from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from APP.models import Articulo, Publicador, Portal
from APP.views import BaseView
from APP_PANEL.forms import CustomAuthenticationForm, ArticleForm





@login_required
def dummy(request):
    render(request, "")

class PanelView(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Articulo.objects.all()
    template_name = "APP_PANEL/article_list.html"    
    context_object_name = "articles"


def detail(request):
    articulo = Articulo.objects.get(pk=2)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()

            return redirect('detail')
    else:
        form= ArticleForm(instance=Articulo)

    return render(request, "APP_PANEL/article_list.html",{"articulo": articulo, "form": form})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ['title' , 'content','content_upload', 'author', 'image', 'is_headline', 'image','genero','size', 'date_published']
    template_name = "APP_PANEL/article_form.html"
    success_url = reverse_lazy("panel-page")


class ArticleUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Articulo
    fields = ['title', 'content','content_upload', 'author', 'image', 'is_headline', 'image','genero','size', 'date_published']
    success_url = reverse_lazy('panel-page')
    

class ArticleDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Articulo 
    success_url = reverse_lazy('panel-page')
    

class PanelLogin(LoginView):
    template_name = "APP_PANEL/panel_login.html"
    next_page = reverse_lazy("raiz")
    authentication_form = CustomAuthenticationForm

class PanelLogout(LogoutView):
    template_name = 'APP/index.html'


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'APP_PANEL/crear_cuenta_form.html'
  success_url = reverse_lazy('panel-page')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"


class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Publicador
    template_name = "user_profile/user_detail.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])



class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "user_profile/user_form.html"
    fields = ["email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

def adopcion(request):
    article = Articulo.objects.all()
    return render(request,'APP_PANEL/adoption.html',{'article': article})


def mostrar_login(request):
    return render(request, "APP_PANEL/panel_login.html", {})

def macho(request):
    macho = Articulo.objects.filter(genero='macho')
    return render(request,'APP_PANEL/filtromacho.html' ,{'macho': macho})

def hembra(request):
    hembra = Articulo.objects.filter(genero='hembra')
    return render(request,'APP_PANEL/filtrohembra.html' ,{'hembra': hembra})


def chico(request):
    chico = Articulo.objects.filter(size='chico')
    return render(request,'APP_PANEL/chico.html',{'chico': chico})

def mediano(request):
    mediano = Articulo.objects.filter(size='mediano')
    return render(request,'APP_PANEL/mediano.html',{'mediano': mediano})

def grande(request):
    grande = Articulo.objects.filter(size='grande')
    return render(request,'APP_PANEL/grande.html',{'grande': grande})


class ArticleDetailView(DetailView):

    model = Articulo
    template_name ="APP_PANEL/article_detail.html"
    

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])