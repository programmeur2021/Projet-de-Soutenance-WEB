from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

TYPE_UTILISATEUR = (('Centre', 'Centre'), ('Parrain', 'Parrain') )
class Utilisateur(AbstractUser):
	type_utilisateur = models.CharField(max_length=25,choices=TYPE_UTILISATEUR,default = "Sélectionner")
	photo_utilisateur = models.FileField(upload_to='media/Utilisateur',blank=True)
	confirmation_password = models.CharField(max_length=50)

