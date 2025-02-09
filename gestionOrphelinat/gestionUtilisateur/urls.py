
from django.urls import path
from django.views.generic import RedirectView
from gestionUtilisateur.views import *
app_name='gestionUtilisateur'
urlpatterns = [
    path('modificationUser/<int:pk>', modifier_utilisateur, name ="modificationUser"),
    path('editerUser/<int:pk>', editer_utilisateur, name ="editerUser"),
    path('listeUser/', Liste_utilisateur, name ="listeutilisateur"),
    path('inscription/', Inscription, name ="inscription"),
]