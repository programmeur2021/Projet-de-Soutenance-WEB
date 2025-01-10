from django.urls import path
from .views import *

urlpatterns = [
  path("ajoutactivite/", EnregistreActivites, name = "ajoutactivite"),
  path("consulteractivite/<int:pk>", ConsulterActivite, name = "consulteractivite"),
  path("listeactivite/", listeActivite, name = "listeactivite"),
  path("editerActivite/<int:pk>", editerActivite, name = "editerActivite"),
  path("modificationActivite/<int:id_activite>", ModifierActivite, name = "modificationActivite"),
  path("suppressionActivite/<int:id_activite>", SupprimerActivite, name = "suppressionActivite"),
  path("rechercherActivite", RechercherActivite, name = "rechercherActivite"),
  path("filtrerActivite/", RechercherActivite, name = "filtrerActivite"),
]