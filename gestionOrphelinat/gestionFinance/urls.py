

from django.urls import path
from .views import *

urlpatterns = [
    path("ajoutCaisse/", AjoutCaisse, name = "ajoutCaisse"), 
    path("ajoutBanque/", AjoutBanque, name = "ajoutBanque"), 
    path("listeCaisse/", ListeCaisse, name = "listeCaisse"), 
    path("listeBanque/", ListeBanque, name = "listeBanque"), 
    path("consulterCaisse/<int:pk>", ConsulterCaisse, name = "consulterCaisse"), 
    path("consulterBanque/<int:pk>", ConsulterBanque, name = "consulterBanque"), 
    path("supprimerCaisse/<int:identifiant>", SupprimerCaisse, name = "supprimerCaisse"), 
    path("supprimerBanque/<int:code>", SupprimerBanque, name = "supprimerBanque"), 
    path("editerCaisse/<int:code>", EditerCaisse, name = "editerCaisse"), 
    path("editerBanque/<int:identifiant>", EditerBanque, name = "editerBanque"), 
    path("modificationCaisse/<int:codes>", ModificationCaisse, name = "modificationCaisse"), 
    path("modificationBanque/<int:cod>", ModificationBanque, name = "modificationBanque"), 
    path("rechercherCaisse", RechercherCaisse, name = "rechercherCaisse"), 
    path("rechercherBanque", RechercherBanque, name = "rechercherBanque"), 
    
]