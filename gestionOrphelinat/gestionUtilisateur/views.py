from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from gestionParrainage.models import *
from gestionActivites.models import Activites
from gestionUtilisateur.forms import FormAuthentification, FormUser
from gestionUtilisateur.models import TYPE_UTILISATEUR, Utilisateur
from django.core.paginator import Paginator

# Permet d'acceder au tableau de bord de l'application
@login_required
def home(request):
    liste_centre = Centre_Orphelinat.objects.all()
    liste_orphelin = Enfant.objects.all()
    liste_parrain = Parrain.objects.all()
    liste_parrainer = Parrainage.objects.all()
    liste_activite = Activites.objects.all()
    liste_utilisateur = Utilisateur.objects.all()
    liste_utilisateur = Dons.objects.all()
    nombre_centre = 0
    nombre_orphelin = 0
    nombre_parrain = 0
    nombre_activite = 0
    nombre_parrainer = 0
    nombre_utilisateur = 0
    nombre_parrainer = 0
    nombre_don = 0
    # if nombre_centre is not None:
    nombre_centre = liste_centre.count()
    nombre_orphelin = liste_orphelin.count()
    nombre_parrain = liste_parrain.count()
    nombre_parrainer = liste_parrainer.count()
    nombre_activite = liste_activite.count()
    nombre_utilisateur = liste_utilisateur.count()
    nombre_parrainer = liste_parrainer.count()
    nombre_don = liste_parrainer.count()
    # else:
    #     nombre_centre = 0
    context = {
        'nombre_centre' : nombre_centre, 
        'nombre_orphelin' : nombre_orphelin,
        'nombre_parrain' : nombre_parrain,
        'nombre_parrainer' : nombre_parrainer,
        'nombre_activite' : nombre_activite,
        'nombre_utilisateur' : nombre_utilisateur,
        'nombre_parrainer' : nombre_parrainer,
        'nombre_don' : nombre_don,
               }
    return render(request, 'dashboard.html', context)
# =============================================================================
# Gestion de l'authentification des utilisateurs
def Loginuser(request):

	flogin = FormAuthentification()
	
	if request.method == 'POST':
		username = request.POST['username'] #Fait réference aux input du template
		password = request.POST['password']
		user = authenticate(request, username=username, password=password) # Permet de vérifier l'authenticité des informations saisies

		if user is not None and password:
			login(request, user)
			# id_user=request.user.id
			# type=request.user.type_utilisateur
			return redirect('/accueil/') # En cas de connexion reussie, je redirige l'utilisateur vers la page d'accueil de l'application, i.e le dashboard
		else:
			messages.error(request, 'Veuillez vérifier vos informations d\'authentification')
			return redirect('/') # En cas d'erreur, je le maintiens sur la page de connexion (page d'entree de l'application
	else:
		pass
	return render(request, 'login.html',dict(form=flogin))

# =============================================================================
def logoutuser(request):
	logout(request)
	messages.success(request, 'Vous êtes maintenant déconnecté')
	return redirect('/')
# =============================================================================
# Gestion des comptes utilisateurs
# @login_required
#@permission_required
def Inscription(request):
	if request.method == 'POST':
		utilisateur = FormUser(request.POST)
		if utilisateur.is_valid():		
			password1 = utilisateur.data['password'] #Fait réference aux input du template
			password2 = utilisateur.data['confirmation_password'] #Fait réference aux input du template
			
			for msg in utilisateur.errors.as_data():
				if msg == 'confirmation_password' and password1 == password2:
					messages.error(request, 'Le mot de passe saisi {} n\'est pas suffisamment fort'.format(password1))
				elif msg == 'confirmation_password' and password1 != password2:
					messages.error(request, 'Vos mots de passe ne sont pas identiques')			
			
			utilisateur.save()
			id_user=Utilisateur.objects.latest('id')
			type=Utilisateur.objects.get(id=id_user.id)
			type_user=type.type_utilisateur
			messages.success(request, 'Compte utilisateur ajouté avec succès')
			utilisateur = FormUser()
			if type_user== TYPE_UTILISATEUR[0][0]:
				return redirect('gestionParrainage:ajoutCentre', id_user.id)
			elif type_user==TYPE_UTILISATEUR[1][0]:
				return redirect('gestionParrainage:ajoutParrain', id_user.id)
				#return redirect(request,'gestionParrainage/ajoutParrain.html', {'id_user': 'id_user'})
				# return redirect('gestionParrainage:ajoutParrain', id_user)
		else:
			# Permet de verifier que le mot de passe saisi est conforme dans les deux champs de saisie
			password1 = utilisateur.data['password']
			password2 = utilisateur.data['confirmation_password']  #Fait réference aux input du template
			
			for msg in utilisateur.errors.as_data():
				if msg == 'confirmation_password' and password1 == password2:
					messages.error(request, 'Le mot de passe saisi {} n\'est pas suffisamment fort'.format(password1))
				elif msg == 'confirmation_password' and password1 != password2:
					messages.error(request, 'Vos mots de passe ne sont pas identiques')
	else:
		utilisateur = FormUser()
	return render(request, 'gestionUtilisateur/inscription.html', dict(form=utilisateur))
# =============================================================================

@login_required
#@permission_required
def Liste_utilisateur(request):
	listeuser = Utilisateur.objects.all().order_by('last_name')
	pageuser = Paginator(listeuser, 5)
	numpage = request.GET.get('page')
	listeuser = pageuser.get_page(numpage)
	context = {'listeuser': listeuser}
	return render(request, 'liste_utilisateur.html', context)
# =============================================================================

@login_required
def editer_utilisateur(request, pk):
	utilisateur = Utilisateur.objects.get(id=pk)
	return render(request, 'modification_login.html', dict(utilisateur=utilisateur))

# =============================================================================
# @login_required
# def details_utilisateur(request, pku):
# 	utilisateur = Utilisateur.objects.get(id=pku)
# 	return render(request, 'afficher_details_utilisateur.html', dict(utilisateur=utilisateur))

# =============================================================================
@login_required
def modifier_utilisateur(request, pk):
	if request.method == 'POST':
		if request.POST['password'] != request.POST['confirmation_password']:
			messages.warning(request, 'Vos mots de passe ne sont pas conformes')
		else:
			utilisateur = Utilisateur.objects.get(id=pk)
			utilisateur.username = request.POST['username']
			utilisateur.password = request.POST['password']
			utilisateur.confirmation_password = request.POST['confirmation_password']
			utilisateur.email = request.POST['email']
			utilisateur.first_name = request.POST['first_name']
			utilisateur.last_name = request.POST['last_name']
			utilisateur.photo_user = request.FILES.get('new_photo_user')
			utilisateur.save()
			return redirect('/listeutilisateur/')
	else:
		return redirect('/listeutilisateur/')
# =============================================================================

# @login_required
# def supprimer_utilisateur(request, idu):
# 	utilisateur = Utilisateur.objects.get(id=idu)
# 	utilisateur.delete()
# 	messages.success(request, 'Utilisateur supprimé avec succès')
# 	return redirect('/listeutilisateur/')
# =============================================================================