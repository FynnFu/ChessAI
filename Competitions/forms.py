from django import forms
from .models import TournamentModel


class TournamentForm(forms.ModelForm):
    class Meta:
        model = TournamentModel
        fields = ['name', 'password', 'type', 'data']
