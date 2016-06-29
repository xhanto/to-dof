from lists.models import UserProfile, List
from django.contrib.auth.models import User
from django import forms
from lists.choices import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Nom d\'utilisateur',
            'email' : 'Adresse email',
            'password': 'Mot de passe',
        }

class UserProfileForm(forms.ModelForm):
    server = forms.ChoiceField(choices = SERVER_CHOICES, initial='0', widget=forms.Select())
    class Meta:
        model = UserProfile
        fields = ('server', 'mp')
        labels = {
            'server': 'Serveur',
            'mp': 'Pseudo in-game',
        }
class NewListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name','public')
        labels = {
            'list_name': 'Nom',
            'public' : 'Liste publique'
        }
        help_texts = {
            'public': 'Une liste publique permet aux autres utilisateurs de voir votre liste.<br> Ils pourront aussi voir votre serveur et nom in-game si ceux-ci figurent sur votre profil.',
        }

class EditListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name','server')
        labels = {
            'list_name': 'Nom',
            'server' : 'Serveur'
        }
