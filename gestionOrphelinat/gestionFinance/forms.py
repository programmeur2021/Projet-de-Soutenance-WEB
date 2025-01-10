from django import forms
from .models import *
from gestionParrainage.forms import FormCentre

#====================================================================
class FormCaisse(forms.ModelForm):
    class Meta:
        model = Caisse
        fields = ("type_operation", "description_operation", "montant_operation",
                  "id_centre")
        
        labels = {
            "type_operation" : "Type opération",
            "description_operation" : "Description opération",
            "montant_operation" : "Montant opération",
            "id_centre" : "Centre",   
        }
        
        widgets = {
            "type_operation" : forms.Select(attrs={'class' : 'form-control',"title" : "Sélectionner le type de l'opération "}, choices=TYPE_OPERATION_CAISSE),
            "description_operation" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Descripiton de l'opération", "title" : "saisissez la description de l'opération "}),
            "montant_operation" : forms.NumberInput(attrs={'class' : 'form-control', "placeholder" : "Montant de l'opération", "title" : "saisissez le montant de l'opération "}),
            "id_centre" :  forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom du Centre", "title" : "sélectionner un Centre"})
        }
        
        def __init__(self, *args, **kwargs):
            super(FormCaisse,self).__init__(*args, **kwargs)
            self.fields["id_centre"].empty_label = "Selectionner"
           
#======================================================================= 
class FormBanque(forms.ModelForm):
    class Meta:
        model = Banque
        
        fields = ("libelle_operation","type_operation", "montant", "numero_banque", "id_centre")
        
        labels = {
            "libelle_operation" : "Nom de la Banque",
            "type_operation" : "Type Opération",
            "montant" : "Montant ",
            "numero_banque" : "Numéro de Compte",
            "id_centre" : "Centre",
        }
        
        widgets = {
            "libelle_operation" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Libellé de l'opération", "title" : "Sasissiez le libelle"}),
            "type_operation" : forms.Select(attrs={"class" : "form-control", "title" : "Sélectionner le type de l'opération"}, choices=TYPE_OPERATION_BANQUE),
            "montant" : forms.NumberInput(attrs={"class" : "form-control", "placeholder" : "Montant", "title" : "Saisissez le montant de l'opération"}),
            "numero_banque" : forms.NumberInput(attrs={"class" : "form-control", "placeholder" : "Numéro Bancaire", "title" : "Sasissez le numéro bancaire"}),
            "id_centre" :  forms.Select(attrs={"class" : "form-control", "placeholder" : "Nom du Centre", "title" : "sélectionner un Centre"})
        }
        
    def __init__(self, *args, **kwargs):
        super(FormBanque, self).__init__(*args, **kwargs)
        self.fields["id_centre"].empty_label = "Selectionner"