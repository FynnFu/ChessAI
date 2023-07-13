from django.urls import path, include

from Competitions.views import *

urlpatterns = [
    path('', home, name='home'),
    path('add-tournament/', add_tournament, name='add_tournament'),
    path('join-the-tournament/<int:tournament_id>', join_the_tournament, name='join_the_tournament'),
    path('tournament/<int:tournament_id>', tournament_panel, name='tournament_panel')
]
