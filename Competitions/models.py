import json
import os

from django.db import models

from ChessAI import settings


# Create your models here.
class TournamentFormsModel(models.Model):
    # Тип соревнования
    type = models.CharField(max_length=100)
    # Название типа
    type_name = models.CharField(max_length=100)
    # Файл фильтрации значений
    file = models.FileField(upload_to='filters/')

    def __str__(self):
        return self.type_name


class TournamentModel(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # Название соревнования
    name = models.CharField(max_length=100)
    # Пароль для изменения
    password = models.CharField(max_length=100)
    # Тип соревнования
    type = models.ForeignKey(TournamentFormsModel, on_delete=models.CASCADE)
    # Файл с результатами
    data = models.FileField(upload_to='game_saves/', default='game_saves/default.json')
    # Подключение игроков
    connecting_players = models.BooleanField(default=True)
    # Открытая группа
    open = models.BooleanField(default=False)
    # Создаст дату и время при создании объекта
    date_add = models.DateTimeField(auto_now_add=True)
    # Создаст дату и время при изменении объекта
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

