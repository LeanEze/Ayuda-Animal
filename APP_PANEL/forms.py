from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from APP.models import Articulo

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'

class ArticleForm(ModelForm):
    class Meta:
        model= Articulo
        fields = ['title','content']

