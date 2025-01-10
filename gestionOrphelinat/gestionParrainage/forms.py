from django import forms
from .models import *

 #========================Formulaire du Centre====================================
class FormCentre(forms.ModelForm):
    class Meta:
        model = Centre_Orphelinat
        fields = ('raison_sociale', 'contact1', 'contact2', 'email', 'localisation', 'logo', 'responsable', 'date_creation', 'capacite')
        labels = { "raison_sociale" : "Nom de l'Orphelinat",
                  "contact1" : "Téléphone 1",
                  "contact2" : "Téléphone 2",
                  "email" : "Adresse E-mail",
                  "localisation" : "Localisation/Adresse",
                  "logo": 'Logo de l\'Orphelinat',
                  "responsable" : "Responsable Orphelinat" ,
                  "date_creation" : "Date de Création",
                  "capacite" : "Capacité d'accueil"
                  }
        widgets = { 
                    "raison_sociale" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Raison sociale/Nom Orphelinat", "title" : "saisissez le nom de l'orphelinat"}),
                    "contact1" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Contact 1", "title" : "saisissez le téléphone 1"}),
                    "contact2" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Contact 2", "title" : "saisissez le téléphone 2"}),
                    "email" : forms.EmailInput(attrs={'class' : 'form-control', "placeholder" : "Adresse e-mail", "title" : "saisissez l'adresse email"}),
                    "localisation" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "localisation orphelinat", "title" : "saisissez votre localisation"}),
                    "logo": forms.FileInput(attrs={'class' : 'form-control', "title" : "Importer le logo du centre"}),
                    "responsable" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Responsable du centre", "title" : "Le responsable"}),
                    "date_creation" : forms.DateInput(attrs={'class' : 'form-control', "placeholder" : "Date de création", "title" : "date de création", "type" : "date"}),
                    "capacite" : forms.NumberInput(attrs={'class' : 'form-control', "placeholder" : "Capacité d'accueil", "title" : "saisissez la capacite d'accueil"}),
                  }
     
    def __init__(self, *args, **kwargs):
        super(FormCentre, self).__init__(*args, **kwargs)
        
 #=========================Forumulaire du Parrain===================================
class FormParrain(forms.ModelForm):
    class Meta:
        model = Parrain
        fields = ("nom_par", "adresse_par", "contact_par", "email_par")
        labels = {
            "nom_par" : "Nom du Parrain",
            "adresse_par" : "Adresse du Parrain",
            "contact_par" : "Téléphone du Parrain",
            "email_par" : "Adresse E-mail du Parrain"
        }
        
        widgets = {
            "nom_par" : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Nom du Parrain", "title" : "saisissez le nom du Parrain"}),
            "adresse_par" : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Adresse du Parrain", "title" : "saisissez l'adresse du Parrain"}),
            "contact_par" : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Téléphone du Parrain", "title" : "saisissez le téléphone"}),
            "email_par" : forms.EmailInput(attrs = {"class" : "form-control", "placeholder" : "E-mail du Parrain", "title" : "saisissez l'adresse e-mail du Parrain"}),
        }
          
    def __init__(self, *args, **kwargs):
        super(FormParrain, self).__init__(*args, **kwargs)  
                
#=========================Formulaire des Orphelins===================================

class FormEnfants(forms.ModelForm):
    class Meta:
        model = Enfant
        fields = ("nom_enf", "prenom_enf", "date_admission", "sexe_enf", "statut_enf", 
                  "photo_enf", "date_naissance", "profession_enf", "lieu_naissance", "pere_enf", "mere_enf",
                  "id_centre")
        labels = {
            "nom_enf" : "Nom de l'enfant", 
            "prenom_enf" : "Prénom de l'enfant", 
            "date_admission" : "Date d'admission",
            "sexe_enf" : "Sexe de l'enfant",
            "statut_enf" : "Statut de l'enfant",
            "photo_enf" : "Photo de l'enfant",
            "date_naissance" : "Date de Naissance",
            "profession_enf" : "Profession de l'enfant",
            "lieu_naissance" : "Lieu de Naissance",
            "pere_enf" : "Pere de l'enfant",
            "mere_enf" : "Mere de l'enfant",
            "id_centre" : "Centre",
        }  
        
        widgets = {
            "nom_enf" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Nom de l'enfant", "title" : "saisissez le nom de l'enfant"}),
            "prenom_enf" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Prénom de l'enfant", "title" : "saisissez le prénom de l'enfant"}),
            "date_admission" : forms.DateInput(attrs={"class" : "form-control", "placeholder" : "Date admission", "title" : "saisissez la date d'admission", "type" : "date"}) ,
            "sexe_enf" : forms.Select(attrs={"class" : "form-control", "placeholder" : "Sexe de l'enfant", "title" : "selectionner le sexe"}, choices = SEXE),
            "statut_enf" : forms.Select(attrs={"class" : "form-control", "placeholder" : "Statut de l'enfant", "title" : "sélectionner le statut"}, choices = STATUT_ENFANT),
            "photo_enf" : forms.FileInput(attrs={"class" : "form-control", "title" : "Importer la photo de l'enfant"}),
            "date_naissance" :  forms.DateInput(attrs={"class" : "form-control", "placeholder" : "Date de Naissance", "title" : "saisissez la date de Naissance", "type" : "date"}),
            "profession_enf" :  forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Profession de l'enfant", "title" : "saisissez la profession "}),
            "lieu_naissance" :  forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Lieu de Naissance de l'enfant", "title" : "saisissez le Lieu de Naissance"}),
            "pere_enf" :  forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Nom du Père de l'enfant", "title" : "saisissez le nom du père"}),
            "mere_enf" :  forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Nom de la mère de l'enfant", "title" : "saisissez le nom de la mère"}),
            "id_centre" :  forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom du centre", "title" : "sélectionner l'orphelinat"}),
        }
    def __init__(self, *args, **kwargs):
        super(FormEnfants,self).__init__(*args, **kwargs)
        self.fields["id_centre"].empty_label = "Selectionner"
        self.fields["sexe_enf"].empty_label = "Selectionner"
        self.fields["statut_enf"].empty_label = "Selectionner"
        
 #============================================================
class FormParrainer(forms.ModelForm):
    class Meta:
             model = Parrainage
             fields = ("id_enfant", "id_parrain")
             labels = {
            "id_enfant" : "Enfant",
            "id_parrain" : "Parrain"
        } 
             widgets = {
             "id_enfant" : forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom de l'enfant", "title" : "selectionner l'enfant"}),
             "id_parrain" : forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom du Pararain", "title" : "selectionner le Parrain"})
        }
    def __init__(self, *args, **kwargs):
        super(FormParrainer,self).__init__(*args, **kwargs) 
        self.fields["id_enfant"].empty_label = "Selectionner"
        self.fields["id_parrain"].empty_label = "Selectionner"
    #===========================Formulaire des Dons=================================
class FormDons(forms.ModelForm):
    class Meta:
        model = Dons
        fields = ("type_dons","description_don", 
                  "montant_don", "id_centre", "id_parrain")
        labels = {
            "type_dons" : "Type du Dons",
            "description_don" : "Description du Dons",
            "montant_don" : "Montant du Dons",
            "id_centre" : "Centre",
            "id_parrain" : "Parrain"
        }
        
        widgets = {
            "type_dons" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Type de dons", "title" : "saisissez le type"}) ,
            "date_don" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Date du don", "title" : "saisissez date du Don"}) ,
            "description_don" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Description du Don", "title" : "saisissez la description"}) ,
            "montant_don" : forms.NumberInput(attrs={"class" : "form-control", "placeholder" : "Montant du Don", "title" : "saisissez le montant"}) ,
            "id_centre" : forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom de l'orphelinat", "title" : "Centre"}) ,
            "id_parrain" : forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom du Pararain", "title" : "Parrain"})
        }
    
    def __init__(self, *args, **kwargs):
        super(FormDons,self).__init__(*args, **kwargs)
        self.fields["id_centre"].empty_label = "Selectionner"
        self.fields["id_parrain"].empty_label = "Selectionner"

    #==========================================================================