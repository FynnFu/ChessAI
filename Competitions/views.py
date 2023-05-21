import json

from django.conf import settings
from django.core.files.base import ContentFile, File
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Competitions.forms import *
from Competitions.models import *


# Create your views here.
def home(request):
    host = request.build_absolute_uri()
    context = {
        'host': host
    }
    return render(request, 'competitions/home.html', context)


def add_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)

        if form.is_valid():
            # Сохранение объекта турнира в базе данных
            form.save()
            return redirect('tournament_list')
    else:
        file = File(open(settings.MEDIA_ROOT + "/game_saves/test.json", 'rb'))
        form = TournamentForm(initial={'data': file})
        print(form['data'].value())
    context = {
        'form': form,
    }
    return render(request, 'competitions/add_tournament.html', context)
