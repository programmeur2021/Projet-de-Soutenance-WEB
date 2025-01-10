
from django import forms
from .models import *

class FormActivites(forms.ModelForm):
    class Meta:
        model = Activites
        fields = ('description_act', 'date_act', 'id_centre', 'rapport_act')
        labels = { "description_act" : "Description de l'activité",
                  "date_act" : "Date de l'activité",
                  "id_centre" : "Centre", 
                  "rapport_act" : "Rapport d'activité"
                  }
        widgets = { 
                    "description_act" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Description de l'activité", "title" : "Faite la description de votre activité"}),
                    "date_act" : forms.DateInput(attrs={'class' : 'form-control', "placeholder" : "Date de début de l'activité", "title" : "saisissez la date de début de l'activité", "type" : "date"}),
                    "rapport_act" : forms.FileInput(attrs={'class' : "form-control", "title" : "Uploader le rapport"}),
                    "id_centre" : forms.Select(attrs={'class' : 'form-control', "placeholder" : "Nom du centre", "title" : "sélectionner l'orphelinat"}),
                  }
     
    def __init__(self, *args, **kwargs):

        super(FormActivites, self).__init__(*args, **kwargs)

        self.fields["id_centre"].empty_label = "Selectionner"

