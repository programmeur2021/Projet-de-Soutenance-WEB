from django.contrib import admin
from .models import Centre_Orphelinat, Parrain, Dons, Enfant, Parrainage
# Register your models here.

admin.site.register(Centre_Orphelinat)
admin.site.register(Parrain)
admin.site.register(Dons)
admin.site.register(Enfant)
admin.site.register(Parrainage)
