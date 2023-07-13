from django import forms
from .models import TournamentModel


class TournamentForm(forms.ModelForm):
    class Meta:
        model = TournamentModel
        fields = ['name', 'password', 'connecting_players', 'type', 'open']


class JoinTheTournament(forms.ModelForm):
    accept_rules = forms.BooleanField()
