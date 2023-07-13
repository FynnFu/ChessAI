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
            form = TournamentForm(request.POST)
            if form.is_valid():
                tournament = form.save(commit=False)

                name = tournament.name
                tournament_model = TournamentModel.objects.filter(name=name)

                if len(tournament_model) == 0:
                    # Создание имени файла и пути
                    file_name = f"{name}.json"
                    file_path = str(settings.BASE_DIR) + '/game_saves/' + file_name

                    # Преобразование данных в формат JSON
                    data = {
                        'name': tournament.name,
                        'password': tournament.password,
                        'type': tournament.type.type,
                        'usernames': []
                        # Добавьте другие поля, если необходимо
                    }
                    json_data = json.dumps(data, ensure_ascii=False)

                    # Создание файла с данными
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(json_data)

                    # Сохранение пути к файлу в поле 'data' модели TournamentModel
                    tournament.data = 'game_saves/' + file_name
                    # Сохранение объекта турнира в базе данных
                    form.save()
                    return redirect('tournament_panel', tournament.id)
                else:
                    form = TournamentForm()
                    error = "Данное имя уже занято! Используйте другое"
                    context = {
                        'form': form,
                        'error': error
                    }
                    return render(request, 'competitions/add_tournament.html', context)

    else:
        form = TournamentForm()
    context = {
        'form': form,
    }
    return render(request, 'competitions/add_tournament.html', context)


def tournament_panel(request, tournament_id: int):
    host = 'https://' + request.get_host() + f'join-the-tournament/'
    print(host)
    tournament = TournamentModel.objects.get(id=tournament_id)
    context = {
        'tournament': tournament
    }
    return render(request, 'competitions/tournament.html', context)


def tournament_panel_player(request, tournament_id: int):
    return redirect('home')


def join_the_tournament(request, tournament_id: int):
    tournament = TournamentModel.objects.get(id=tournament_id)
    if request.user.is_authenticated:
        if tournament.connecting_players:
            form = JoinTheTournament()
            if request.method == 'POST':
                print(request.user.username)
                return redirect('home')
            else:
                context = {
                    'tournament': tournament,
                    'form': form
                }
                return render(request, 'competitions/join_the_tournament.html', context)
    else:
        return redirect('login')
