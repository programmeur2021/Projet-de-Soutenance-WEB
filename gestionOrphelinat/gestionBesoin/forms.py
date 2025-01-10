from django import forms
from .models import *

class  FormBesoin(forms.ModelForm):
    class Meta:
        model= Besoins
        fields={'description_bes','type_bes','id_centre'}
        labels={
            "description_bes":"La demande",
            "types_bes":"le type du besoin",
            "id_centre":"le centre concerné",
        }
        widgets={
            "description_bes" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "Que voulez-vous ", "title" : "saisissez le besoin"}),
            "types_besoin" : forms.TextInput(attrs={'class' : 'form-control', "placeholder" : "le type du besoin", "title" : "saisissez le type du besoin"}),
            "id_centre": forms.Select(attrs={'class' : 'form-control', "placeholder" : "Le nom du centre", "title" : "saisissez le nom du centre"}),
        }
    def __init__(self, *args, **kwargs):
        super(FormBesoin, self).__init__(*args, **kwargs)    