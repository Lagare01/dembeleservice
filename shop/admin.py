from django.contrib import admin
from .models import category, product, Commande

# Register your models here.
admin.site.site_header = "Commerce Général"
admin.site.site_title = "Dembele S"
admin.site.index_title = "Dembele Service"


class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom', 'date_added')
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'prix', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('prix', 'category',)
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'Nom', 'Email', 'address', 'Ville','Quartier', 'Pays','total', 'Numéro_téléphone', 'date_commande')
    
    

admin.site.register(product, AdminProduct)
admin.site.register(category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
