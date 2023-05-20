from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    host = request.build_absolute_uri()
    context = {
        'host': host
    }
    return render(request, 'competitions/home.html', context)


def create_tournament(request):
    return HttpResponse('Test Page')
