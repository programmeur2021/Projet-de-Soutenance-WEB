"""
URL configuration for gestionOrphelinat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from gestionUtilisateur.views import  logoutuser,home, Loginuser

urlpatterns = [
    path('', Loginuser, name='connexion'),
    path('deconnexion/', logoutuser, name='deconnexion'),
    path('accueil/', home, name='accueil'),
    path('logout/', RedirectView.as_view(url ='/admin/logout/')),
    path('admin/', admin.site.urls),
    path('Utilisateur/', include("gestionUtilisateur.urls")),
    path('Parrainage/', include("gestionParrainage.urls")),
    path('Finance/', include("gestionFinance.urls")),
    path('Besoin/', include("gestionBesoin.urls")),
    path('Activite/', include("gestionActivites.urls")),
    path('Activite/', include("gestionActivites.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
