import django_filters
from APP.models import Articulo

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Articulo
        fields = {'genero':['exact'],'size':['exact'],'age':['exact']}