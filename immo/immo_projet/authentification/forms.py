from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    nom = forms.CharField(max_length=100, required=True)
    prenom = forms.CharField(max_length=100, required=True)
    numero = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Utilisateur
        fields = ['username', 'nom', 'prenom', 'email', 'numero', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nom = self.cleaned_data['nom']
        user.prenom = self.cleaned_data['prenom']
        user.numero = self.cleaned_data['numero']
        user.role = 'client'  # Définit le rôle par défaut
        if commit:
            user.save()
        return user
