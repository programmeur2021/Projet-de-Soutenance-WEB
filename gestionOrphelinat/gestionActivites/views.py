from django.shortcuts import redirect

from django.shortcuts import render 
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib import messages
from django.utils.dateparse import parse_date
from datetime import datetime as d

# Create your views here.

def EnregistreActivites(request):
    if request.method == "POST":
        form = FormActivites(request.POST)
        if form.is_valid() :
            descr = request.POST['description_act']
            dte = request.POST['date_act']
            dte = d.strptime(dte, '%Y-%m-%d')
            code = request.POST['id_centre']
            centre = Centre_Orphelinat.objects.get(id=code)
            rapport = request.FILES.get('rapport_act')
            activite = Activites(description_act = descr, date_act = dte, id_centre=centre, rapport_act=rapport)
            activite.save()
            messages.success(request, "L'activité à été ajouté avec succès")
            form = FormActivites()
        else :
            messages.warning(request, "Veuillez Renseigner votre Activité")
    else : 
        form = FormActivites()
    return render(request, 'gestionActivites/ajoutActivites.html', {"form" : form})

#*********************************************************************************
def ConsulterActivite(request,pk):
    activité = Activites.objects.get(id=pk)
    return render(request, "gestionActivites/consulterActivite.html", {"infoActivite" : activité})

#*********************************************************************************
def listeActivite(request): 
    listeactivite = Activites.objects.select_related('id_centre').all().order_by("date_fin")
    pageformat=Paginator(listeactivite, 10)
    numpage= request.GET.get('page')
    listeactivite = pageformat.get_page(numpage)
    return render(request, "gestionActivites/listeactivite.html", {"infoActivite" : listeactivite})
 
#*********************************************************************************
def editerActivite(request, pk):
    Activite = Activites.objects.get(id=pk)
    return render(request, "gestionActivites/modifierActivite.html", {"activite" : Activite})

#*********************************************************************************
def ModifierActivite(request, id_activite):
    if request.method == "POST":
        activite = Activites.objects.get(id=id_activite)
        activite.description_act = request.POST.get("description_act")
        date_a = request.POST.get('date_act')
        activite.date_act = d.strptime(date_a, '%Y-%m-%d')
        if request.POST.get('rapport_act') != "":
            activite.rapport_act = request.FILES.get('rapport_act')
        else : 
            pass
        # code = request.POST.get('id_centre')
        # centre = Centre_Orphelinat.objects.get(id=code)
        # activite.id_centre = centre
        activite.save()
        return redirect ("../listeactivite/")
    else :
        return redirect("../listeactivite/")
    
    
#*********************************************************************************
def SupprimerActivite(request, id_activite):
    Activite = Activites.objects.get(id=id_activite)
    Activite.delete()
    return redirect("../listeactivite/")

#*********************************************************************************
def ConsulterActivite(request,pk):
    activité = Activites.objects.get(id=pk)
    return render(request, "gestionActivites/consulterActivite.html", {"infoActivite" : activité})

#*********************************************************************************
def listeActivite(request): 
    listeactivite = Activites.objects.select_related('id_centre').all().order_by("date_act")
    pageformat=Paginator(listeactivite, 5)
    numpage= request.GET.get('page')
    listeactivite = pageformat.get_page(numpage)
    return render(request, "gestionActivites/listeactivite.html", {"infoActivite" : listeactivite})
 
#*********************************************************************************
def editerActivite(request, pk):
    Activite = Activites.objects.get(id=pk)
    return render(request, "gestionActivites/modifierActivite.html", {"activite" : Activite})
    
#*********************************************************************************
def SupprimerActivite(request, id_activite):
    Activite = Activites.objects.get(id=id_activite)
    Activite.delete()
    return redirect("../listeactivite/")
# =================================== 1ère Méthode Rechercher une Activitée========================================
# def RechercherActivite(request):
#     date_debut = request.GET.get('datedebut')
#     date_fin=request.GET.get('datefin')
    
#     if (date_debut != "" and date_debut is not None) and (date_fin != "" and date_fin is not None): 
#         dbut = d.strptime(date_debut, '%Y-%m-%d')
#         dfin = d.strptime(date_fin, '%Y-%m-%d')
#         liste = Activites.objects.filter(date_act__range=(dbut, dfin)).all()
#         pageformat=Paginator(liste, 10)
#         numpage= request.GET.get('page')
#         liste = pageformat.get_page(numpage)
#     context= {'activite' : liste}
#     return render(request, 'gestionActivites/listeactivite.html', context)

#=================================2eme  Méthode de rechercher par période =============================================

def RechercherActivite(request):
    date_debut = request.GET.get('datedebut')
    date_fin=request.GET.get('datefin')
    liste = []
    if (date_debut != "" and date_debut is not None) and (date_fin != "" and date_fin is not None): 
        dbut = d.strptime(date_debut, '%Y-%m-%d')
        dfin = d.strptime(date_fin, '%Y-%m-%d')
        liste = Activites.objects.filter(date_act__gte=dbut, date_act__lte=dfin).all().order_by("date_act")
        pageformat=Paginator(liste, 5)
        numpage= request.GET.get('page')
        liste = pageformat.get_page(numpage)
    context= {'activite' : liste}
    return render(request, 'gestionActivites/listeactivite.html', context)