from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="page_accueil"),
    path('apropos', Apropos, name="Apropos"),
    path('propriete', propriete, name="proprete"),
    path('propert_single',propert_single, name="propert_single"),
    path('services', services, name="services"),
    path('service_detail',service_detail, name="service_detail" ),
    path('contact', contact, name="contact"),
    path('admin/', admin.site.urls, name="admin"),
]
