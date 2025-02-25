from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('admin', 'Admin'),
    ]
    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100, blank=False) 
    mail = models.CharField(max_length=100, blank=False) 
    numero = models.CharField(max_length=100, blank=False) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    # Pour résoudre le conflit avec le modèle 'auth.User'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilisateur_set',  # Change le nom pour éviter le conflit
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilisateur_set',  # Change le nom pour éviter le conflit
        blank=True,
    )

    def __str__(self):
        return self.username
