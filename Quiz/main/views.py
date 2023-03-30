from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .filters import *


## Create your views here.

def index(request):
    return render(request,'base_generic.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form': form}

    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('/')

    return render(request, 'main/registration/register.html', context)


class KategorijeList(ListView):
    model = Kategorija

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = KategorijaFilter(self.request.GET, queryset=self.get_queryset())
        return context


class KvizoviList(ListView):
    model = Kviz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = KvizFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PitanjaList(ListView):
    model = Pitanje

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PitanjaFilter(self.request.GET, queryset=self.get_queryset())
        return context

class OpisiList(ListView):
    model = OpisPitanja

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OpisFilter(self.request.GET, queryset=self.get_queryset())
        return context

#Create
def createKategorija(request):

    form = KategorijaForm()
    if request.method == 'POST':
        print(request.POST)
        form = KategorijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kategorije')

    context = {'form': form}

    return render(request,'main/kategorija_form.html', context)


def createKviz(request):

    form = KvizForm()
    if request.method == 'POST':
        print(request.POST)
        form = KvizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kvizovi')

    context = {'form': form}

    return render(request,'main/kviz_form.html', context)


def createPitanje(request):

    form = PitanjeForm()
    if request.method == 'POST':
        print(request.POST)
        form = PitanjeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pitanja')

    context = {'form': form}

    return render(request,'main/pitanje_form.html', context)

def createOpis(request):

    form = OpisForm()
    if request.method == 'POST':
        print(request.POST)
        form = OpisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/opisi')

    context = {'form': form}

    return render(request,'main/opispitanja_form.html', context)

#Update
def updateKategorija(request, pk):

    kategorija = Kategorija.objects.get(id=pk)
    form = KategorijaForm(instance=kategorija)
    if request.method == 'POST':
        print(request.POST)
        form = KategorijaForm(request.POST, instance=kategorija)
        if form.is_valid():
            form.save()
            return redirect('/kategorije')

    context = {'form': form}

    return render(request,'main/kategorija_form.html', context)

def updateKviz(request, pk):

    kviz = Kviz.objects.get(id=pk)
    form = KvizForm(instance=kviz)
    if request.method == 'POST':
        print(request.POST)
        form = KvizForm(request.POST, instance=kviz)
        if form.is_valid():
            form.save()
            return redirect('/kvizovi')

    context = {'form': form}

    return render(request,'main/kviz_form.html', context)

def updatePitanje(request, pk):

    pitanje = Pitanje.objects.get(id=pk)
    form = PitanjeForm(instance=pitanje)
    if request.method == 'POST':
        print(request.POST)
        form = PitanjeForm(request.POST, instance=pitanje)
        if form.is_valid():
            form.save()
            return redirect('/pitanja')

    context = {'form': form}

    return render(request,'main/pitanje_form.html', context)

def updateOpis(request, pk):

    opis = OpisPitanja.objects.get(id=pk)
    form = OpisForm(instance=opis)
    if request.method == 'POST':
        print(request.POST)
        form = OpisForm(request.POST, instance=opis)
        if form.is_valid():
            form.save()
            return redirect('/opisi')

    context = {'form': form}

    return render(request,'main/opispitanja_form.html', context)

#Delete

def deleteKategorija(request, pk):
    kategorija = Kategorija.objects.get(id=pk)
    context = {'item':kategorija}

    if request.method == 'POST':
        kategorija.delete()
        return redirect('/kategorije')
    return render(request,'main/kategorija_delete.html', context)

def deleteKviz(request, pk):
    kviz = Kviz.objects.get(id=pk)
    context = {'item':kviz}

    if request.method == 'POST':
        kviz.delete()
        return redirect('/kvizovi')
    return render(request,'main/kviz_delete.html', context)

def deletePitanje(request, pk):
    pitanje = Pitanje.objects.get(id=pk)
    context = {'item':pitanje}

    if request.method == 'POST':
        pitanje.delete()
        return redirect('/pitanja')
    return render(request,'main/pitanje_delete.html', context)

def deleteOpis(request, pk):
    opis = OpisPitanja.objects.get(id=pk)
    context = {'item':opis}

    if request.method == 'POST':
        opis.delete()
        return redirect('/opisi')
    return render(request,'main/opispitanja_delete.html', context)
