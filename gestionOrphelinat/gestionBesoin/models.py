from django.db import models
from gestionParrainage.models import Centre_Orphelinat

# Create your models here.

class Besoins(models.Model):
    description_bes = models.CharField(max_length = 100)
    type_bes = models.CharField(max_length =80)
    date_bes = models.DateField(auto_now = True)
    id_centre = models.ForeignKey(Centre_Orphelinat,on_delete = models.CASCADE, default="Sélectionner")

    def __str__(self):
        return '{} {} {}'.format(self.description_bes,self.type_bes,self.date_bes)
    
    @property
    def centre (self):
        return '{}'.format(self.id_centre)