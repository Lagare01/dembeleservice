from django.db import models

#Create your modeles here:
class category(models.Model):
    nom = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.nom
   
class product(models.Model):
    title = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()
    category =models.ForeignKey(category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images')
    date_added = models.DateTimeField(auto_now= True)
    class Meta :
        ordering = ['-date_added']
    def __str__(self):
        return self.title
    
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    Nom = models.CharField(max_length=150)
    Email = models.EmailField()
    address = models.CharField(max_length=200)
    Ville = models.CharField(max_length=200)
    Quartier = models.CharField(max_length=200)
    Pays = models.CharField(max_length=300)
    Numéro_téléphone = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_commande']
        
    def __str__(self):
        return self.Nom








    
    
    
   