from django.contrib import admin
from django.urls import path,include, re_path
from APP import views
from APP_PANEL.views import PanelLogout , adopcion 
from APP.views import error_404_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    #BARRA NAV
    path('admin/', admin.site.urls),
    path('', views.mostrar_inicio,name='raiz'),
    path('donaciones/', views.mostrar_donaciones, name='donaciones'),
    path('contactenos/', views.mostrar_contactenos, name='contactenos'),
    path('transito/', views.mostrar_transito, name='transito'),
    path('', include('APP_PANEL.urls')),
]
handler404 = 'APP.views.error_404_view'

