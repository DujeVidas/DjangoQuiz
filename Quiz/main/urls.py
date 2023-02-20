from django.urls import path
from main.views import *
from . import views
from django.views.generic import RedirectView

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('',views.index,name = 'index'),
    #path('', RedirectView.as_view(url='kvizovi')),
    path('kategorije', KategorijeList.as_view(), name = 'kategorije'),
    path('kvizovi', KvizoviList.as_view(), name = 'kvizovi'),
    path('pitanja', PitanjaList.as_view(), name = 'pitanja'),
    path('opisi', OpisiList.as_view(), name = 'opisi'),
]