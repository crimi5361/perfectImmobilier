from django.urls import path
from .views import  inscription
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
    path('Authentification/inscription', inscription),
]
