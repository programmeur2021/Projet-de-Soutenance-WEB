from django.db import models
from gestionParrainage.models import Centre_Orphelinat
# Create your models here.
TYPE_OPERATION_BANQUE = (("Débit", "Débit"), ("Crédit", "Crédit"))
TYPE_OPERATION_CAISSE = (("Entrée", "Entrée"), ("Sortie", "Sorties"))

class Caisse(models.Model):
    type_operation = models.CharField(max_length = 100, choices = TYPE_OPERATION_CAISSE, default = "Entrée")
    description_operation = models.CharField(max_length = 100)
    montant_operation = models.DecimalField(max_digits=12,decimal_places = 2)
    date_operation = models.DateField(auto_now= True)
    id_centre = models.ForeignKey(Centre_Orphelinat, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.description_operation,self.montant_operation, self.date_operation}"
    
    @property
    def centre(self):
        return "{self.id_centre}"

#=======================================================================

class Banque(models.Model):
    libelle_operation = models.CharField(max_length = 100)
    type_operation = models.CharField(max_length = 50, choices = TYPE_OPERATION_BANQUE, null=True, default = "Crédit")
    date_operation = models.DateField(auto_now = True)
    montant = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    numero_banque = models.IntegerField()
    id_centre = models.ForeignKey(Centre_Orphelinat, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.libelle_operation,self.date_operation, self.numero_banque}"
    
    @property
    def centre(self):
        return f"{models.id_centre}"
    