from django.db import models
from gestionParrainage.models import Centre_Orphelinat

# Create your models here.

class Activites(models.Model):
    description_act = models.CharField(max_length = 100)  
    date_act = models.DateField()      
    id_centre = models.ForeignKey(Centre_Orphelinat, on_delete = models.CASCADE, default="Sélectionner")
    rapport_act = models.FileField(upload_to='media/Rapport', blank=True)

    def __str__(self):
     return '{} {} {}'.format(self.description_act, self.date_debut, self.date_fin)

    @property
    def centre(self):
        return '{}'.format(self.id_centre)