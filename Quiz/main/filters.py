import django_filters
from .models import *


CHOICES = (
        ('ascending', 'Ascending'),
        ('descending','Descending')
    )


class KategorijaFilter(django_filters.FilterSet):

    ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES, method ='filter_by_order')

    class Meta:
        model = Kategorija
        fields = {
            'nazivKategorije' : ['icontains']
        }
    
    def filter_by_order(self,queryset,name,value):
        expression ='nazivKategorije' if value == 'ascending' else '-nazivKategorije'
        return queryset.order_by(expression)


class KvizFilter(django_filters.FilterSet):

    ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES, method ='filter_by_order')

    class Meta:
        model = Kviz
        fields = {
            'naziv': ['icontains'],
            'kategorija': ['exact']
        }

    def filter_by_order(self,queryset,name,value):
        expression ='naziv' if value == 'ascending' else '-naziv'
        return queryset.order_by(expression)

    

class PitanjaFilter(django_filters.FilterSet):

    ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES, method ='filter_by_order')

    class Meta:
        model = Pitanje
        fields = {
            'naziv': ['icontains'],
            'kviz': ['exact']
        }

    def filter_by_order(self,queryset,name,value):
        expression ='naziv' if value == 'ascending' else '-naziv'
        return queryset.order_by(expression)

class OpisFilter(django_filters.FilterSet):
        
    ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES, method ='filter_by_order')

    class Meta:
        model = OpisPitanja
        fields = {
            'tekst': ['icontains']
        }
    
    def filter_by_order(self,queryset,name,value):
        expression ='tekst' if value == 'ascending' else '-tekst'
        return queryset.order_by(expression)
    