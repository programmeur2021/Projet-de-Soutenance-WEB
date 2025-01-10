from django.db import models

# Create your models here.
SEXE = (('Sélectionner', 'Sélectionner un sexe'),('Masculin', 'Masculin'), ('Feminin', 'Feminin'))
STATUT_ENFANT = (('Sélectionner', 'Sélectionner un statut'),('Orphelin de Père', 'Orphelin de Père'), ('Orphelin de Mère', 'Orphelin de Mère'), ('Adopté', 'Adopté'), ('Orphelin Père/Mère', 'Orphelin Père/Mère'))

#====================================Centre Orphelinat=====================================
class Centre_Orphelinat(models.Model):
    raison_sociale = models.CharField(max_length=100)
    contact1 = models.CharField(max_length=25)
    contact2 = models.CharField(max_length=25, blank=True)
    email = models.EmailField()
    localisation = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/Centres', blank=True)
    responsable = models.CharField(max_length=55, blank=True)
    date_creation = models.DateField()
    capacite = models.IntegerField()
    
    def __str__(self):
     return '{} {} {}'.format(self.raison_sociale, self.contact1, self.email)

#=======================================Parrain======================================
class Parrain(models.Model):
    nom_par = models.CharField(max_length=60)
    adresse_par = models.CharField(max_length=55)
    contact_par = models.CharField(max_length=35)
    email_par = models.EmailField()
    
    def __str__(self):
        return '{} {} {}'.format(self.nom_par, self.contact_par, self.email_par)
#==============================Orphelin====================================================
class Enfant(models.Model):
    nom_enf = models.CharField(max_length=65)
    prenom_enf = models.CharField(max_length= 65)
    date_admission = models.DateField()
    sexe_enf = models.CharField(max_length=35, choices = SEXE, default = "Sélectionner")
    statut_enf = models.CharField(max_length = 250, choices = STATUT_ENFANT, default = "Sélectionner")
    photo_enf = models.FileField(upload_to ='media/Enfants', blank= True)
    date_naissance = models.DateField()
    profession_enf = models.CharField(max_length = 100)
    lieu_naissance = models.CharField(max_length = 65)
    pere_enf = models.CharField(max_length = 64)    
    mere_enf = models.CharField(max_length = 60)  
    id_centre = models.ForeignKey(Centre_Orphelinat,on_delete = models.CASCADE)
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.nom_enf, self.prenom_enf, self.statut_enf, self.pere_enf, self.mere_enf)  
    
    @property
    def centre(self):
        return '{}'.format(self.id_centre)
#================================Dons====================================================
class Dons(models.Model):
    type_dons = models.CharField(max_length = 10)
    date_don = models.DateField(auto_now = True)
    description_don = models.CharField(max_length = 100)
    montant_don = models.DecimalField(max_digits=12, decimal_places = 2)
    id_centre = models.ForeignKey(Centre_Orphelinat, on_delete= models.CASCADE)
    id_parrain = models.ForeignKey(Parrain,on_delete= models.CASCADE)
    
    def __str__(self):
        return '{}{}{}'.format(self.type_don, self.description_don, self.montant_don)
    
    @property
    def parrain(self):
        return '{}'.format(self.id_parrain)
    
    @property
    def centre(self):
        return '{}'.format(self.id_centre)
#===============================Parrainage=================================================
class Parrainage(models.Model):
    id_enfant = models.ForeignKey(Enfant, on_delete= models.CASCADE)
    id_parrain = models.ForeignKey(Parrain,on_delete= models.CASCADE)
    date_parrainage = models.DateField(auto_now= True)
    
    def __str__(self):
        return '{}{}{}'.format(self.id_enfant, self.id_parrain, self.date_parrainage)
    
    
    @property
    def enfant(self):
        return '{}'.format(self.id_enfant)
    
    @property
    def parrain(self):
        return '{}'.format(self.id_parrain)
#===============================================================================