# from django.http import HttpResponse
from django.shortcuts import render
from .models import Rest


def index(request):
    rest = Rest.objects.all
    return render(request, 'map/map_index.html', {'rest':rest})
