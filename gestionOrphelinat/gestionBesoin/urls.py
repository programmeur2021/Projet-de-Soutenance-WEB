from django.urls import path
from .views import *

urlpatterns = [
    path("ajoutbesoin/", EnregistreBesoin, name = "ajoutbesoin"),  
    path("listebesoin/", ListeBesoin, name ="listebesoin"),
    path("consulterBesoin/<int:pk>", ConsulterBesoin, name = "consulterBesoin"),
    path("editerbesoin/<int:pk>" , editerBesoin, name = "editerbesoin"),
    path("modifierbesoin/<int:id_besoin>" , ModifierBesoin, name = "modifierbesoin"),
    path("suppressionbesoin/<int:id_besoin>" , SupprimerBesoin, name = "suppressionbesoin"),
    
]