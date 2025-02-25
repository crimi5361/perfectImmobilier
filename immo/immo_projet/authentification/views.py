from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from Authentification.models import Utilisateur  # type: ignore # Utilise ton modèle personnalisé

def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        username = request.POST.get('username')
        email = request.POST.get('email')
        numero = request.POST.get('numero')
        mot_de_passe = request.POST.get('password1')
        confirmation_mot_de_passe = request.POST.get('password2')

        # Vérification des mots de passe
        if mot_de_passe != confirmation_mot_de_passe:
            return HttpResponse("Les mots de passe ne correspondent pas !")

        # Vérifier si le nom d'utilisateur est déjà pris
        if Utilisateur.objects.filter(username=username).exists():
            messages.error(request, "Le nom d'utilisateur est déjà utilisé.")
            return render(request, 'Authentification/inscription.html')

        # Création de l'utilisateur
       
        messages.success(request, "Inscription réussie !")
        return redirect('page_accueil')

    return render(request, 'Authentification/inscription.html')
