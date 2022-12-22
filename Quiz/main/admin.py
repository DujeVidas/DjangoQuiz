from django.contrib import admin
from .models import *
# Register your models here.

model_list = [Kategorija,Kviz,Pitanje,OpisPitanja]

admin.site.register(model_list)