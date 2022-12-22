from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import *

## Create your views here.
def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
    # primjetiti korištenje HTML-a

class KategorijeList(ListView):
    model = Kategorija

class KvizoviList(ListView):
    model = Kviz


class PitanjaList(ListView):
    model = Pitanje

class OpisiList(ListView):
    model = OpisPitanja

