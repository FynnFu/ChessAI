from django.contrib import admin
from .models import *


# Регистрация моделей в админке
@admin.register(TournamentFormsModel)
class TournamentFormsModelAdmin(admin.ModelAdmin):
    list_display = ('type', 'type_name', 'file')
    list_filter = ('type',)  # Фильтр по полю 'type'


@admin.register(TournamentModel)
class TournamentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'data', 'date_add', 'date_change')
    list_filter = ('type',)  # Фильтр по полю 'type'
    search_fields = ('name',)  # Поиск по полю 'name'
    readonly_fields = ('date_add', 'date_change')  # Поля только для чтения


# Дополнительные настройки админки
admin.site.site_header = 'Администрирование Турниров'  # Заголовок админки
admin.site.index_title = 'Добро пожаловать в админку Турниров'  # Заголовок главной страницы админки
admin.site.site_title = 'Админка'  # Заголовок вкладки браузера для админки
