from django.urls import path
from main.views import *
from django.views.generic import RedirectView

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', RedirectView.as_view(url='kvizovi')),
    path('kategorije', KategorijeList.as_view()),
    path('kvizovi', KvizoviList.as_view()),
    path('pitanja', PitanjaList.as_view()),
    path('opisi', OpisiList.as_view()),
]