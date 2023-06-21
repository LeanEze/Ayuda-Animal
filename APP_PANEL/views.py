from django.http import HttpResponse
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
from APP_PANEL.forms import CustomAuthenticationForm
from .filters import ListingFilter
from PIL import Image, ImageOps


@login_required
def dummy(request):
    render(request, "")

class PanelView(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Articulo.objects.all()
    template_name = "APP_PANEL/article_list.html"    
    context_object_name = "articles"

    def get_context_data(request):
        article = Articulo.objects.all()
        listing_filter = ListingFilter(request.GET , queryset=article)
        context = {
            'listing_filter': listing_filter
            }
        return render(request,'APP_PANEL/article_list.html', context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ['title' ,'content', 'author', 'is_headline','thumbnail','image', 'image1', 'image2','animal','genero','size','age','date_published']
    template_name = "APP_PANEL/article_form.html"
    success_url = reverse_lazy("adopcion")
    def form_valid(self, form):
        thumbnail = form.cleaned_data['thumbnail']
        image = form.cleaned_data['image']
        image1 = form.cleaned_data['image1']
        image2 = form.cleaned_data['image2']
        # Validar el tamaño de la imagen
        if image.size > 2 * 1024 * 1024:  # 2 MB
            form.add_error('image', 'La imagen debe tener un tamaño máximo de 2MB.')
            return self.form_invalid(form)
        if image1.size > 2 * 1024 * 1024:  # 2 MB
            form.add_error('image1', 'La imagen debe tener un tamaño máximo de 2MB.')
            return self.form_invalid(form)
        if image2.size > 2 * 1024 * 1024:  # 2 MB
            form.add_error('image2', 'La imagen debe tener un tamaño máximo de 2MB.')
            return self.form_invalid(form)
        if thumbnail.size > 2 * 1024 * 1024:  # 2 MB
            form.add_error('thumbnail', 'La imagen debe tener un tamaño máximo de 2MB.')
            return self.form_invalid(form)
        # Redimensionar la imagen si es necesario
        return super().form_valid(form)




class ArticleUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Articulo
    fields = ['title', 'content', 'author', 'is_headline','thumbnail', 'image', 'image1', 'image2','animal', 'genero', 'size', 'age', 'date_published']
    success_url = reverse_lazy('adopcion')
    

class ArticleDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Articulo 
    success_url = reverse_lazy('adopcion')
    

class PanelLogin(LoginView):
    template_name = "APP_PANEL/panel_login.html"
    next_page = reverse_lazy("raiz")
    authentication_form = CustomAuthenticationForm

class PanelLogout(LogoutView):
    template_name = 'APP/index.html'


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'APP_PANEL/crear_cuenta_form.html'
  success_url = reverse_lazy('raiz')
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
    article = Articulo.objects.all().order_by('title')
    listing_filter = ListingFilter(request.GET , queryset=article)
    context = {
        'listing_filter': listing_filter
    }
    return render(request,'APP_PANEL/adoption.html', context)

#Genera pantalla inicio sesion
def mostrar_login(request):
    return render(request, "APP_PANEL/panel_login.html", {})

#Muestra articulos seleccionado en adopcion y lo muestra en template detalles
class ArticleDetailView(DetailView):
    
    #indica el model a utilizar
    model = Articulo
    #indica el template a mostrar
    template_name ="APP_PANEL/article_detail.html"
    

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
    

