# Creation du formulaire d'ajout des utilisateurs
from django import forms
from .models import Utilisateur
class FormUser(forms.ModelForm):
	class Meta:
		model = Utilisateur
		fields = ('username', 'email', 'password', 'confirmation_password', 'first_name', 'last_name', 'photo_utilisateur')
		labels = {
			'username': 'Nom utilisateur',
			'email': 'Email/Adresse electronique',
			'password': 'Mot de passe',
			'confirmation_password': 'Confirmation',
			'first_name': 'Prénom utilisateur',
			'last_name': 'Nom utilisateur',
			'photo_utilisateur': 'Photo profil'
                }
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom utilisateur', 'title': 'Saisissez le nom de l\'utilisateur'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email/Adresse electronique', 'title': 'Saisissez un email correct', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\\".[a-z]{2,4}$'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'title': 'Saisissez votre mot de passe'}),
			'confirmation_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe', 'title': 'Saisissez votre mot de passe à nouveau'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom(s)', 'title': 'Saisissez votre prénom(s)'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom famille', 'title': 'Saisissez votre nom de famille'}),
			'photo_utilisateur': forms.FileInput(attrs={'class': 'form-control', 'title': 'Importer la photo de profil de l\'utilisateur', 'accept': 'image/png'})
            }

	def __init__(self, *args, **kwargs):
		super(FormUser, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = False
		self.fields['last_name'].required = False

		
# Gestion du formulaire d'authentification
class FormAuthentification(forms.ModelForm):
	class Meta:
		model = Utilisateur
		fields = ('username', 'password')
		labels = {
			'username': 'Nom utilisateur',
			'password': 'Mot de passe'
                }
		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Nom utilisateur', 'title': 'Saisissez le nom d\'utilisateur'}),
			'password': forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'title': 'Saisissez le mot de passe'})
                }

	def __init__(self, *args, **kwargs):
		super(FormAuthentification, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['class'] = 'form-control'