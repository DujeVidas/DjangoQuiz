from django.forms import ModelForm
from .models import *

class KategorijaForm(ModelForm):
    class Meta:
        model = Kategorija
        fields = '__all__'


class KvizForm(ModelForm):
    class Meta:
        model = Kviz
        fields = '__all__'

class PitanjeForm(ModelForm):
    class Meta:
        model = Pitanje
        fields = '__all__'

class OpisForm(ModelForm):
    class Meta:
        model = OpisPitanja
        fields = '__all__'
        