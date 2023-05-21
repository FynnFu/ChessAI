from django.urls import path, include

from Competitions.views import *

urlpatterns = [
    path('', home, name='home'),
    path('add-tournament/', add_tournament, name='add-tournament'),
]
