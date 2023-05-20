from django.urls import path, include

from Competitions.views import *

urlpatterns = [
    path('', home, name='home'),
    path('create-tournament/', create_tournament, name='create-tournament'),
]
