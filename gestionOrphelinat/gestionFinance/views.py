from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
# Create your views here.

#==========================GESTION DE LA CAISSE=======================================

#*******************ENREGISTRER UNE CAISSE**********************
def AjoutCaisse(request):
    if request.method == "POST":
        form = FormCaisse(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "La Caisse à été ajouté avec succès")
            form = FormCaisse()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    
    else : 
        form = FormCaisse()
    return render(request, 'gestionFinance/ajoutCaisse.html', {"form" : form})
       
#********************************LA LISTE DE LA CAISSE********************************* 
def ListeCaisse(request):
    liste =  Caisse.objects.select_related('id_centre').all().order_by("date_operation")   
    pageformat = Paginator(liste, 10)
    numeropage = request.GET.get('page')
    liste = pageformat.get_page(numeropage)
    return render(request, "gestionFinance/listeCaisse.html", {"listeCaisse" : liste})

#***********************************CONSULTER LA CAISSE***********************************

def ConsulterCaisse(request, pk):
    caisse = Caisse.objects.get(id=pk)
    return render(request, "gestionFinance/consulterCaisse.html", {"infoCaisse" : caisse})

#******************SUPPRIMER UNE CAISSE********************
def SupprimerCaisse(request, identifiant):
    caisse = Caisse.objects.get(id=identifiant)
    caisse.delete()
    return redirect("../listeCaisse")
#**********************EDITER UNE CAISSE*******************************
def EditerCaisse(request, code):
    caisse = Caisse.objects.get(id=code)
    return render(request, 'gestionFinance/modificationCaisse.html', {'editer': caisse})
#********************MODIFIATION D'UNE CAISSE**********************
def ModificationCaisse(request, codes):
    if request.method == 'POST':
        caisse = Caisse.objects.get(id=codes)
        caisse.type_operation = request.POST.get('type_operations')
        caisse.description_operation = request.POST.get('description')
        caisse.montant_operation = request.POST.get('montant_oper')
        caisse.date_operation = request.POST.get('date_operation')
        codes = request.POST.get('id_centre_id')
        centre = Centre_Orphelinat.objects.get(id=codes)
        caisse.id_centre = centre
        caisse.save()
        return redirect("../listeCaisse")
    else :
        return redirect("../listeCaisse")
#****************************************************************************
def RechercherCaisse(request):
    operation = request.GET.get('type_operation')
    description = request.GET.get('description_operation')
    date_operation = request.GET.get('date_operation')
    
    if operation != "" or operation is not None:
        liste = Caisse.objects.filter(type_operation__icontains = operation).all().order_by('description_operation')
    if description != "" or description is not None:
          liste = Caisse.objects.filter(description_operation__icontains = description).all().order_by('description_operation')
    if date_operation:
          liste = Caisse.objects.filter(date_operation__icontains = parse_date(date_operation)).all().order_by('description_operation')
    pageformat = Paginator(liste, 6)
    numero_page = request.GET.get('page')
    liste = pageformat.get_page(numero_page)
    return render(request, 'gestionFinance/listeCaisse.html', {'listerechercher' : liste})

#=================================GESTION DE LA BANQUE========================================== 
def AjoutBanque(request):
    if request.method == "POST":
        form = FormBanque(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "La Banque à été ajouté avec succès")
            form = FormBanque()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    
    else : 
        form = FormBanque()
    return render(request, 'gestionFinance/ajoutBanque.html', {"form" : form})
        
#***************************LISTE DE LA BANQUE**********************************
def ListeBanque(request):
    liste =  Banque.objects.all().order_by("date_operation")   
    pageformat = Paginator(liste, 10)
    numeropage = request.GET.get('page')
    liste = pageformat.get_page(numeropage)
    return render(request, "gestionFinance/listeBanque.html", {"listeBanque" : liste})

#*******************CONSULTATION D'UNE BANQUE********************************
def ConsulterBanque(request, pk):
    banque = Banque.objects.get(id=pk)
    return render(request, "gestionFinance/consulterBanque.html", {"infoBanque" : banque})

#*******************SUPPRIMER UNE BANQUE*************************
def SupprimerBanque(request, code):
    banque = Banque.objects.get(id=code)
    banque.delete()
    return redirect("../listeBanque")

#*******************EDITER UNE BANQUE*************************
def EditerBanque(request, identifiant):
    banque = Banque.objects.get(id=identifiant)
    return render(request, 'gestionFinance/modificationBanque.html', {'editer': banque})

#**************************MODIFICATION D'UNE BANQUE**********************

def ModificationBanque(request, cod):
    if request.method == 'POST':
        banque = Banque.objects.get(id=cod)
        banque.libelle_operation = request.POST.get('libelle_op')
        banque.type_operation = request.POST.get('type_opera')
        banque.date_operation = request.POST.get('date_operat')
        banque.montant = request.POST.get('montant')
        banque.numero_banque = request.POST.get('numero_banque')
        codes = request.POST["id_ctre"]
        centre = Centre_Orphelinat.objects.get(id=codes)
        banque.id_centre = centre
        banque.save()
        return redirect("../listeBanque")
    else :
        return redirect("../listeBanque")

#==========================Rechercher Banque =======================
def RechercherBanque(request):
    operation = request.GET.get('type_operation')
    description = request.GET.get('libelle_operation')
    date_operation = request.GET.get('date_operation')
    
    if operation != "" or operation is not None:
        liste = Banque.objects.filter(type_operation__icontains = operation).all().order_by('date_operation')
    if description != "" or description is not None:
          liste = Banque.objects.filter(libelle_operation__icontains = description).all().order_by('date_operation')
    if date_operation:
          liste = Banque.objects.filter(date_operation__icontains = parse_date(date_operation)).all().order_by('date_operation')
    pageformat = Paginator(liste, 6)
    numero_page = request.GET.get('page')
    liste = pageformat.get_page(numero_page)
    return render(request, 'gestionFinance/listeBanque.html', {'listerechercher' : liste})
#==========================================================================================

