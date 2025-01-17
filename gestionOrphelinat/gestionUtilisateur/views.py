
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from gestionUtilisateur.forms import FormAuthentification, FormUser
from gestionUtilisateur.models import Utilisateur
from django.core.paginator import Paginator

# Permet d'acceder au tableau de bord de l'application
@login_required
def home(request):
    
	return render(request, 'dashboard.html')

# Gestion de l'authentification des utilisateurs
def Loginuser(request):

	flogin = FormAuthentification()
	
	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password) # Permet de vérifier l'authenticité des informations saisies

		if user is not None and password:
			login(request, user)
			return redirect('/accueil/') # En cas de connexion reussie, je redirige l'utilisateur vers la page d'accueil de l'application, i.e le dashboard
		else:
			messages.error(request, 'Veuillez vérifier vos informations d\'authentification')
			return redirect('/') # En cas d'erreur, je le maintiens sur la page de connexion (page d'entree de l'application
	else:
		pass

	return render(request, 'login.html',dict(form=flogin))


def logoutuser(request):
	logout(request)
	messages.success(request, 'Vous êtes maintenant déconnecté')
	return redirect('/')


# Gestion des comptes utilisateurs
@login_required
#@permission_required
def enregistrer_utilisateur(request):

	utilisateur = FormUser()
	if request.method == 'POST':
		utilisateur = FormUser(request.POST)
		if utilisateur.is_valid():
			
			password1 = utilisateur.data['password1']
			password2 = utilisateur.data['password2']
			
			for msg in utilisateur.errors.as_data():
				if msg == 'password2' and password1 == password2:
					messages.error(request, 'Le mot de passe saisi {} n\'est pas suffisamment fort'.format(password1))
				elif msg == 'password2' and password1 != password2:
					messages.error(request, 'Vos mots de passe ne sont pas identiques')			
			
			utilisateur.save()
			messages.success(request, 'Compte utilisateur ajouté avec succès')
			utilisateur = FormUser()
		else:
			# Permet de verifier que le mot de passe saisi est conforme dans les deux champs de saisie
			password1 = utilisateur.data['password1']
			password2 = utilisateur.data['password2']
			
			for msg in utilisateur.errors.as_data():
				if msg == 'password2' and password1 == password2:
					messages.error(request, 'Le mot de passe saisi {} n\'est pas suffisamment fort'.format(password1))
				elif msg == 'password2' and password1 != password2:
					messages.error(request, 'Vos mots de passe ne sont pas identiques')
	else:
		pass


	return render(request, 'register.html', dict(form=utilisateur))


@login_required
#@permission_required
def liste_utilisateur(request):
	
	listeuser = Utilisateur.objects.all().order_by('last_name')

	pageuser = Paginator(listeuser, 5)
	numpage = request.GET.get('page')
	listeuser = pageuser.get_page(numpage)
	
	context = {'listeuser': listeuser}
	
	return render(request, 'liste_utilisateur.html', context)


@login_required
def editer_utilisateur(request, pku):
	utilisateur = Utilisateur.objects.get(id=pku)
	return render(request, 'modifier_utilisateur.html', dict(utilisateur=utilisateur))

@login_required
def details_utilisateur(request, pku):
	utilisateur = Utilisateur.objects.get(id=pku)
	return render(request, 'afficher_details_utilisateur.html', dict(utilisateur=utilisateur))

@login_required
def modifier_utilisateur(request, idu):

	if request.method == 'POST':

		if request.POST['password1'] != request.POST['password2']:
			messages.warning(request, 'Vos mots de passe ne sont pas conformes')
		else:
			utilisateur = Utilisateur.objects.get(id=idu)
			utilisateur.username = request.POST['username']
			utilisateur.password1 = request.POST['password1']
			utilisateur.password2 = request.POST['password2']
			utilisateur.email = request.POST['email']
			utilisateur.first_name = request.POST['first_name']
			utilisateur.last_name = request.POST['last_name']
			utilisateur.photo_user = request.FILES.get('new_photo_user')
			utilisateur.save()
			return redirect('/listeutilisateur/')
	else:
		return redirect('/listeutilisateur/')


@login_required
def supprimer_utilisateur(request, idu):
	utilisateur = Utilisateur.objects.get(id=idu)
	utilisateur.delete()
	messages.success(request, 'Utilisateur supprimé avec succès')
	return redirect('/listeutilisateur/')