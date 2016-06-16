from django.contrib import admin
from .models import List, UserProfile,Ressource,Equipement,Arme,Consommable
# Register your models here.

admin.site.register(List)
admin.site.register(UserProfile)
admin.site.register(Ressource)
admin.site.register(Equipement)
admin.site.register(Arme)
admin.site.register(Consommable)
