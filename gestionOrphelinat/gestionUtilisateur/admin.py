from django.contrib import admin
from .models import Utilisateur
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AdministrateursOrphelinat(UserAdmin):
	fieldsets = UserAdmin.fieldsets + ((None,{'fields':('type_utilisateur','photo_utilisateur')}),)

admin.site.register(Utilisateur,AdministrateursOrphelinat)