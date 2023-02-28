from django.urls import path
from shop.views import index, detail, checkout, confirmation


urlpatterns = [
    path('',index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="Vérifier"),
    path('confirmation', confirmation, name= "confirmation"),
]