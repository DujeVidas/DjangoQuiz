from django.urls import path
from main.views import *
from . import views
from django.views.generic import RedirectView

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('',views.index, name = 'index'),
    #path('', RedirectView.as_view(url='kvizovi')),
    path('kategorije', KategorijeList.as_view(), name = 'kategorije'),
    path('kvizovi', KvizoviList.as_view(), name = 'kvizovi'),
    path('pitanja', PitanjaList.as_view(), name = 'pitanja'),
    path('opisi', OpisiList.as_view(), name = 'opisi'),
    
    path('create_kategorija/', views.createKategorija, name='create_kategorija'),
    path('create_kviz/', views.createKviz, name='create_kviz'),
    path('create_pitanje/', views.createPitanje, name='create_pitanje'),
    path('create_opis/', views.createOpis, name='create_opis'),

    path('update_kategorija/<str:pk>/', views.updateKategorija, name='update_kategorija'),
    path('update_kviz/<str:pk>/', views.updateKviz, name='update_kviz'),
    path('update_pitanje/<str:pk>/', views.updatePitanje, name='update_pitanje'),
    path('update_opis/<str:pk>/', views.updateOpis, name='update_opis'),

    path('delete_kategorija/<str:pk>/', views.deleteKategorija, name='delete_kategorija'),
    path('delete_kviz/<str:pk>/', views.deleteKviz, name='delete_kviz'),
    path('delete_pitanje/<str:pk>/', views.deletePitanje, name='delete_pitanje'),
    path('delete_opis/<str:pk>/', views.deleteOpis, name='delete_opis'),
]