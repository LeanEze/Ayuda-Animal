from django.contrib import admin
from django.urls import path,include
from APP import views
from APP_PANEL.views import PanelLogout , adopcion
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    #BARRA NAV
    path('admin/', admin.site.urls),
    path('', views.mostrar_inicio,name='raiz'),
    path('donaciones/', views.mostrar_donaciones, name='donaciones'),
    path('contactenos/', views.mostrar_contactenos, name='contactenos'),
    path('transito/', views.mostrar_transito, name='transito'),
    path('', include('APP_PANEL.urls')),
]

