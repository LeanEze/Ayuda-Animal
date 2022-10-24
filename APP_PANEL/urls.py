from django.urls import path, include
from APP_PANEL import views
from APP_PANEL.views import ArticleDetailView,ArticleCreateView, PanelLogin, PanelLogout, SignUpView, UserProfile, UserUpdate,detail, dummy,PanelView, ArticleUpdateView,ArticleDeleteView 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
  
    #Edicion Staff
    
    path('panel/', PanelView.as_view(), name='panel-page'),
    path('article/create', ArticleCreateView.as_view(), name ="article-create" ),
    path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update" ),
    path('article/<pk>/delete', ArticleDeleteView.as_view(), name ="article-delete" ),
    path(r'^articleDetail/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article-detail'),
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),
    path("signup/", SignUpView.as_view(), name="panel-signup"),
    path("detail/", detail, name="detail"),
    path('dummy', dummy, name="dummy"),
    path("user/<pk>", UserProfile.as_view(), name="user-detail"),
    path("user/<pk>/edit", UserUpdate.as_view(), name="user-update"),
    path('ckeditor/', include('ckeditor_uploader.urls')),    
    path('adopcion/', views.adopcion, name='adopcion'),
    path('filtro/' ,views.macho, name="Macho"),
    path('filtroh/' ,views.hembra, name="Hembra")
    ]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)