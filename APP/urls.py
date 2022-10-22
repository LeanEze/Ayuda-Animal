from django.contrib import admin
from django.urls import path,include
from APP import views
from APP_PANEL.views import PanelLogout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    #BARRA NAV
    path('admin/', admin.site.urls),
    path('', views.mostrar_inicio,name='raiz'),
    path('adopcion/', views.mostrar_adopcion, name='adopcion'),
    path('donaciones/', views.mostrar_donaciones, name='donaciones'),
    path('contactenos/', views.mostrar_contactenos, name='contactenos'),
    # path('login/', views.mostrar_login, name='login'),
    # path("logout/", PanelLogout.as_view (template_name='mi_app/logout.html'), name = 'logout'),
    path('', include('APP_PANEL.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)