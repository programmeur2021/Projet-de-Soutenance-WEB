from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from numbers import Number
from django.utils.dateparse import parse_date
from datetime import datetime as d
# Create your views here
#=========================Gestion des Centres =========================

#*****************************Enregistrer un Centre **********************
def EnregistreCentre(request,id_user):
    if request.method == "POST":
        form = FormCentre(request.POST)
        if form.is_valid() :
            centre = Centre_Orphelinat()
            centre.raison_sociale = request.POST["raison_sociale"]
            centre.contact1 = request.POST["contact1"]
            centre.contact2 = request.POST["contact2"]
            centre.email = request.POST["email"]
            centre.localisation = request.POST["localisation"]
            centre.logo = request.FILES.get("logo")
            centre.responsable = request.POST["responsable"]
            centre.date_creation = request.POST["date_creation"]
            centre.capacite = request.POST["capacite"]
            code_user = Utilisateur.objects.get(id=id_user)
            centre.id_utilisateur=code_user
            centre.save()
            
            #form.save()
            messages.success(request, "Le Centre à été ajouté avec succès")
            form = FormCentre()
            return redirect('/gestionOrphelinat.connexion')
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    
    else : 
        form = FormCentre()
    return render(request, 'gestionParrainage/ajoutCentre.html', {"form" : form})
        
#**************************Liste des Centres **********************************
def ListeCentre(request):
    listecentre =  Centre_Orphelinat.objects.all().order_by("date_creation")   
    pageformat = Paginator(listecentre, 10)
    numpage = request.GET.get('page')
    listecentre = pageformat.get_page(numpage)
    return render(request, "gestionParrainage/listecentre.html", {"listecentre" : listecentre})

#***************************Editer un Centre****************************************
def EditerCentre(request, pk):
    centre = Centre_Orphelinat.objects.get(id=pk)
    return render(request, "gestionParrainage/modifierCentre.html", {"infoCentre" : centre})
 
#**************************Modifier les informations d'un Centre *************************************

def ModifierCentre(request, id_centre):
    if request.method == "POST":
        centre = Centre_Orphelinat.objects.get(id = id_centre)
        centre.raison_sociale = request.POST.get("nom_centre")
        centre.contact1 = request.POST.get("contact1")
        centre.contact2 = request.POST.get("contact2")
        centre.email = request.POST.get("email")
        centre.localisation = request.POST.get("localisation")
        if request.POST.get("logo") != "":
            centre.logo = request.FILES.get("logo")
        else : pass
        centre.responsable = request.POST.get("responsable")
        centre.date_creation = request.POST.get("date_creation")
        centre.capacite = request.POST.get("capacite")
        centre.save()
        return redirect ("../listecentre/")
    else : 
        return redirect ("../listecentre/") 
        
#************************Supprimer un Centre ************************************
def SupprimerCentre(request, id_centre):
    centre = Centre_Orphelinat.objects.get(id=id_centre)
    centre.delete()
    return redirect ('../listecentre/')

#***********************Consulter un Centre ***********************************
def ConsulterCentre(request, pk):
    centre = Centre_Orphelinat.objects.get(id=pk)
    return render(request, "gestionParrainage/consulterCentre.html", {"infoCentre" : centre})

#***************************Rechercher un Centre **************************
def RechercherCentre(request):
    localisation = request.GET.get('localisation')
    listelocalisation = []
    liste_sociale = []
    liste_date = []
    date_creation = request.GET.get('date_creation')
    date_cre = None
    raison_sociale = request.GET.get('raison_sociale')
    if localisation != "" and localisation is not None :
        listelocalisation = Centre_Orphelinat.objects.filter(localisation__icontains=localisation).all().order_by('date_creation')
        pageformat = Paginator(listelocalisation, 10)
        numpage = request.GET.get('page')
        listelocalisation = pageformat.get_page(numpage)
    elif raison_sociale != "" and raison_sociale is not None :
        liste_sociale = Centre_Orphelinat.objects.filter(raison_sociale__icontains=raison_sociale).all().order_by('date_creation')
        pageformat = Paginator(liste_sociale, 10)
        numpage = request.GET.get('page')
        liste_sociale = pageformat.get_page(numpage)
    elif date_cre != "" and date_cre is not None :
        date_cre = d.strptime(date_creation, '%Y-%m-%d')
        liste_date = Centre_Orphelinat.objects.filter(date_creation__iexact=date_cre).all().order_by('date_creation')
        pageformat = Paginator(liste_date, 10)
        numpage = request.GET.get('page')
        liste_date = pageformat.get_page(numpage)
    return render(request, 'gestionParrainage/listecentre.html', {'listeLocalisation': listelocalisation, 'listeRaisonSociale': liste_sociale, 'listeDate': liste_date})
#************************************************************************************************************************************************
#=========================================Gestion des Enfants ================================

#**************************Enregistrer un Enfant******************************
def EnregistreEnfant(request):
    if request.method == "POST":
        form = FormEnfants(request.POST)
        if form.is_valid() :
            enfant = Enfant()
            enfant.nom_enf = request.POST["nom_enf"]
            enfant.prenom_enf = request.POST["prenom_enf"]
            enfant.date_admission = request.POST["date_admission"]
            enfant.sexe_enf = request.POST["sexe_enf"]
            enfant.statut_enf  = request.POST["statut_enf"]
            enfant.photo_enf  = request.FILES.get("photo_enf")
            enfant.date_naissance  = request.POST["date_naissance"]
            enfant.profession_enf = request.POST["profession_enf"]
            enfant.lieu_naissance = request.POST["lieu_naissance"]
            enfant.pere_enf = request.POST["pere_enf"]
            enfant.mere_enf = request.POST["mere_enf"]
            centre = request.POST.get("id_centre")
            print(centre)
            c = Centre_Orphelinat.objects.get(id=centre)
            print(c)
            enfant.id_centre = c
            enfant.save()
            messages.success(request, "L'enfant à été ajouté avec succès")
            form = FormEnfants()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    else : 
        form = FormEnfants()
    return render(request, 'gestionParrainage/ajoutEnfant.html', {"form" : form})

#***************************************Liste des Orphelins**********************************************

def ListeEnfant(request):
    listeEnfant =  Enfant.objects.select_related("id_centre").all().order_by("date_admission") 
    pageformat = Paginator(listeEnfant, 10)
    numpage = request.GET.get('page')
    listeEnfant = pageformat.get_page(numpage)
    return render(request, "gestionParrainage/listeEnfant.html", {"listeEnfant" : listeEnfant})

#************************************Consulter un Orphelins*****************************************

def ConsulterEnfant(request, pk):
    enfant = Enfant.objects.get(id = pk)
    return render(request, "gestionParrainage/consulterEnfant.html", {"infoenfant" : enfant})
        
#*****************************Supprimer un Enfant*********************************

def SupprimerEnfant(request, identifiant):
    enfant = Enfant.objects.get(id=identifiant)
    enfant.delete()
    return redirect('../listeEnfant')
#****************************Rechecher un Enfant **********************************
def RechercherEnfant(request):
    nom = request.GET.get('recherche_nom')
    if nom != "" or nom is not None:
        enfant = Enfant.objects.filter(nom_enf__icontains=nom).all().order_by('nom_enf')
    context = {'enfant' : enfant}
    return render(request, 'gestionParrainage/listeEnfant.html', context)
        
#******************************Edier un Enfant ********************************
def EditerEnfant(request, identifiant):
    enfant = Enfant.objects.get(id=identifiant)
    return render(request, 'gestionParrainage/modificationEnfant.html', {'editer':enfant})

#**********************Modifier les informations d'un Enfant *********************************

def ModificationEnfant(request, identifiant):
    if request.method == 'POST':
        enfant = Enfant.objects.get(id=identifiant)
        enfant.nom_enf = request.POST.get('nom_enf')
        enfant.prenom_enf = request.POST.get('prenom_enf')
        enfant.date_admission = request.POST.get('date_admission')
        enfant.sexe_enf = request.POST.get('sexe_enf')
        enfant.statut_enf = request.POST.get('statut_enf')
        if request.POST.get("photo_enf") != "":
            enfant.photo_enf = request.FILES.get("photo_enf")
        else : 
            pass
        enfant.date_naissance = request.POST.get('date_naissance')
        enfant.profession_enf = request.POST.get('profession_enf')
        enfant.lieu_naissance = request.POST.get('lieu_naissance')
        enfant.pere_enf = request.POST.get('pere_enf')
        enfant.mere_enf = request.POST.get('mere_enf')
        code = request.POST['id_centre_id']
        centre = Centre_Orphelinat.objects.get(id=code)
        enfant.id_centre = centre
        enfant.save()
        return redirect('../listeEnfant')
    return redirect('../listeEnfant')
#************************************************************************************
#=========================================Gestion des Dons ==============================

#*************************Enregistrer un Don********************************
def EnregistreDons(request):
    if request.method == "POST":
        form = FormDons(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "Le Don à été ajouté avec succès")
            form = FormDons()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    else : 
        form = FormDons()
    return render(request, 'gestionParrainage/ajoutDons.html', {"form" : form})

#***********************************Liste des Dons******************************************

def ListeDon(request):
    listedont =  Dons.objects.select_related("id_centre", "id_parrain").all().order_by("date_don") 
    pageformat = Paginator(listedont, 10)
    numeropage = request.GET.get('page')
    listedont = pageformat.get_page(numeropage)
    return render(request, "gestionParrainage/listeDons.html", {"listeDon" : listedont})

#******************************Consulter un Don******************************************
def ConsulterDons(request, pk):
    don = Dons.objects.get(id=pk)
    return render(request, "gestionParrainage/consulterDons.html", {"infoDon" : don})

#******************************Supprimer un Don******************************************
def SupprimerDons(request, pk):
   don = Dons.objects.get(id=pk)
   don.delete()
   return redirect('../listeDon')
#********************************Editer un Don****************************************

def EditerDon(request, pk):
    don = Dons.objects.get(id=pk)
    return render(request, 'gestionParrainage/modificationDon.html', {'editer': don})

#*****************************Modifier les informations d'un Don*******************************************

def ModificationDon(request, codes):
    if request.method == 'POST':
        don = Dons.objects.get(id=codes)
        don.type_dons = request.POST.get('type_dons')
        don.date_don = request.POST.get('date_don')
        don.description_don = request.POST.get('description_don')
        montant = Decimal(request.POST['montant_don'])
        don.montant_don = montant
        code_centre = request.POST['id_centre']
        centre = Centre_Orphelinat.objects.get(id=code_centre)
        don.id_centre = centre
        code_parrain = request.POST['id_parrain']
        parrain = Parrain.objects.get(id=code_parrain)
        don.id_parrain = parrain
        don.save()
        return redirect('../listeDon')
    return redirect('../listeDon')
#********************************* Rechercher un Don **********************
def RechercherDon(request):
    type_don = request.GET.get('type_don')
    description = request.GET.get('description_don')
    date_don = request.GET.get('date_don')
    
    if type_don != "" or type_don is not None :
        liste = Dons.objects.filter(type_dons__icontains=type_don).all().order_by('date_don')
    elif description != "" or description is not None:
        liste = Dons.objects.filter(description_don__icontains=description).all().order_by('date_don')
    if date_don:
          liste = Dons.objects.filter(date_don__icontains = parse_date(date_don)).all().order_by('date_don')
    pageformat = Paginator(liste, 6)
    numero_page = request.GET.get('page')
    liste = pageformat.get_page(numero_page)
    return render(request, 'gestionParrainage/listeDons.html', {'listerechercher' : liste})
#************************************************************************************************
#=================================Gestion des Parrains===============================

#**********************Enregistrer un Parrain**************************************

def EnregistreParrain(request,id_user):
    if request.method == "POST":
        form = FormParrain(request.POST)
        if form.is_valid() :
            parrain = Parrain()
            parrain.nom_par = request.POST["nom_par"]
            parrain.adresse_par = request.POST["adresse_par"]
            parrain.contact_par = request.POST["contact_par"]
            parrain.email_par = request.POST["email_par"]
            code_user = Utilisateur.objects.get(id=id_user)
            parrain.id_utilisateur = code_user
            parrain.save()
            messages.success(request, "Le Parrain à été ajouté avec succès")
            form = FormParrain()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    
    else : 
        form = FormParrain()
    return render(request, 'gestionParrainage/ajoutParrain.html', {"form" : form})

#************************************** Editer un Parrain*********************************

def EditerParrain(request, kl):
    Parrains =Parrain.objects.get(id=kl)
    return render(request, "gestionParrainage/modifierParrain.html", {"infoParrain" : Parrains})

#*************************************Liste des Parrains*****************************************

def ListeParrain(request):
    listeparrainn =  Parrain.objects.all().order_by("contact_par")   
    pageformat = Paginator(listeparrainn, 10)
    numpage = request.GET.get('page')
    listeparrainn = pageformat.get_page(numpage)
    return render(request, "gestionParrainage/listeparrain.html", {"infoParrain" : listeparrainn})

#**************************************Consulter un Parrain******************************************
def ConsulterParrain(request, pk):
    parrain = Parrain.objects.get(id=pk)
    return render(request, "gestionParrainage/consulterParrain.html", {"infoParrain" : parrain})

#***********************************Supprimer un Parrain*****************************************

def SupprimerParrain(request, id_parrain):
    parrain = Parrain.objects.get(id=id_parrain)
    parrain.delete()
    return redirect ('../listeparrain/')

#********************************ModifierParrain********************************

def ModifierParrain(request, id_parrain):
    if request.method == "POST":
        parrain = Parrain.objects.get(id = id_parrain)
        parrain.nom_par = request.POST.get("nom_par")
        parrain.adresse_par = request.POST.get("adresse_par")
        parrain.contact_par = request.POST.get("contact_par")
        parrain.email_par = request.POST.get("email_par")
        parrain.save()
        return redirect ("../listeparrain/")
    else : 
        return redirect ("../listeparrain/") 
    
#*****************************Rechercher un Parrain **********************************************

def RechercherParrain(request):
    nom_par = request.GET.get('nom_par')
    adresse_par = request.GET.get('adresse_parrain')
    contact_par = request.GET.get('contact_par')
    
    if nom_par != "" or nom_par is not None :
        liste = Parrain.objects.filter(nom_par__icontains=nom_par).all().order_by('contact_par')
    if adresse_par != "" or adresse_par is not None :
        liste = Parrain.objects.filter(adresse_par__icontains=adresse_par).all().order_by('contact_par')
    elif contact_par != "" or contact_par is not None :
        liste = Parrain.objects.filter(contact_par__icontains=contact_par).all().order_by('contact_par')
    pageformat = Paginator(liste, 6)
    numpage = request.GET.get('page')
    liste = pageformat.get_page(numpage)
    return render(request, 'gestionParrainage/listeparrain.html',{'listerecherche' : liste})
#********************************************************************************************************************
#====================================Gestion Parrainer===============================

#***************************Enregistrer un Parrainer **********************************
def EnregistreParrainer(request):
    if request.method == 'POST':
        form = FormParrainer(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "Parrainage éffectué avec succès")
            form = FormParrainer()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    else :
        form = FormParrainer()
    return render(request, 'gestionParrainage/ajoutParainer.html', {'form': form})

#******************************Liste des Parrainage***********************

def ListeParrainer(request):
    liste_parrainer = Parrainage.objects.select_related("id_parrain", "id_enfant").all() 
    pageformat = Paginator(liste_parrainer, 10)
    numpage = request.GET.get('page')
    liste_parrainer = pageformat.get_page(numpage)
    return render(request, 'gestionParrainage/listeParrainer.html', {'liste_parrainer' : liste_parrainer})
    
#********************************Consulter Parainage***********************

def ConsulterParainer(request, codes):
        editer = Parrainage.objects.get(id=codes)
        return render(request, 'gestionParrainage/consulterParrainer.html', {'editer': editer})
    
#*******************************Supprimer Parainage***********************

def SupprimerParainer(request, codes):
    parrainer = Parrainage.objects.get(id=codes)
    parrainer.delete()
    return redirect('../listeParainer')

#**********************Editer Parrainer**************************

def editerParainer(request, codes):
    editer = Parrainage.objects.get(id=codes)
    liste_enfant = Enfant.objects.all()
    liste_Parrain = Parrain.objects.all()
    return render(request, 'gestionParrainage/modificationParrainer.html', {'editer': editer, 'enfant' : liste_enfant, 'parrain' : liste_Parrain})

#**********************Supprimer Parrainer**************************

def ModifierParrainer(request, codes):
    if request.method == "POST":
        parrainer = Parrainage.objects.get(id=codes)
        code_enf = request.POST.get('id_enfant')
        enfant = Enfant.objects.get(id=code_enf)
        parrainer.id_enfant = enfant
        code_parrain =  request.POST.get('id_parrain')
        parrain = Parrain.objects.get(id=code_parrain)
        parrainer.id_parrain = parrain
        parrainer.date_parrainage = request.POST.get("date_parrainage")
        parrainer.save()
        return redirect ("../listeParainer/")
    else : 
        return redirect ("../listeParainer/") 
    
#***************************************************************************************

