from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def EnregistreBesoin(request):
    if request.method == "POST":
        form = FormBesoin(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "Le Besoin à été envoyer avec succès")
            form = FormBesoin()
        else :
            messages.warning(request, "Veuillez saisir les données valides")
    
    else : 
        form = FormBesoin()
    return render(request, 'gestionBesoin/ajouter.html', {"form" : form})

#************************************************************
def ListeBesoin(request):
    listebesoin =  Besoins.objects.select_related('id_centre').all().order_by("date_bes")   
    pageformat = Paginator(listebesoin, 10)
    numpage = request.GET.get('page')
    listebesoin = pageformat.get_page(numpage)
    return render(request, "gestionBesoin/listeBesoin.html", {"listebesoin" : listebesoin})

#************************************************************
def ConsulterBesoin(request, pk):
    besoin = Besoins.objects.get(id=pk)
    return render(request, "gestionBesoin/consulteBesoin.html", {"infoBesoin" : besoin})
#************************************************************
def editerBesoin(request ,pk):
    centre= Besoins.objects.get(id=pk)
    return render(request ,"gestionBesoin/modifieBesoin.html", {"infoBesoin": centre})
#************************************************************
def ModifierBesoin(request, id_besoin):
    if request.method == "POST" :
        besoin = Besoins.objects.get(id=id_besoin)
        besoin.description_bes = request.POST.get("description_bes")
        besoin.type_bes = request.POST.get("tybes")
        besoin.date_bes = request.POST.get('date_bes')
        print(Besoins.date_bes)
        code = request.POST.get('id_centre_id')
        centre = Centre_Orphelinat.objects.get(id=code)
        besoin.id_centre = centre
        besoin.save()
        return redirect ("../listebesoin/")
    else :
        return redirect ("../listebesoin/")
 #************************************************************       
def SupprimerBesoin(request, id_besoin):
    besoin = Besoins.objects.get(id=id_besoin)
    besoin.delete()
    return redirect("../listebesoin")