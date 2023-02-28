from django.shortcuts import render
from .models import product, Commande
from django.core.paginator import Paginator
from django.shortcuts import redirect


# Create your views here.
def index(request):
    product_object = product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = product_object.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = product.objects.get(id=myid)
    return  render(request, 'shop/detail.html', {'product': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        Nom = request.POST.get('Nom')
        Email = request.POST.get('Email')
        address = request.POST.get('address')
        Ville = request.POST.get('Ville')
        Quartier = request.POST.get('Quartier')
        Pays = request.POST.get('Pays')
        Numéro_téléphone = request.POST.get('Numéro_téléphone')
        com = Commande(items=items,total=total, Nom=Nom, Email=Email, address= address, Ville=Ville,Quartier=Quartier, Pays=Pays, Numéro_téléphone=Numéro_téléphone)
        com.save()
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        Nom= item.Nom
    return render(request, 'shop/confirmation.html', {'name': Nom})