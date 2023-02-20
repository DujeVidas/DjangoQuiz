from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

## Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


class KategorijeList(ListView):
    model = Kategorija

class KvizoviList(ListView):
    model = Kviz


class PitanjaList(ListView):
    model = Pitanje

class OpisiList(ListView):
    model = OpisPitanja

