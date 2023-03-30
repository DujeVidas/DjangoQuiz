from django.db import transaction
from django.core.management.base import BaseCommand
import random
from main.models import *
from main.factory import (
    KategorijaFactory,
    KvizFactory,
    OpisPitanjaFactory,
    PitanjeFactory,
)

NUM_CATEGORY = 5
NUM_QUIZZES = 5
NUM_QUESTIONS = 2
NUM_EXPLANATION = 2

class Command(BaseCommand):
    help = "Generates test data"
 
    
    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Deleting old data...")

        models = [Kategorija,Kviz,Pitanje,OpisPitanja]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        kategorije = [KategorijaFactory() for _ in range(NUM_CATEGORY)]
        for _ in range(NUM_QUIZZES):
            n = random.randrange(1,NUM_CATEGORY)
            lista = random.sample(kategorije,n)
            kviz = KvizFactory(kategorije=lista)
            kviz.save()
            for _ in range(NUM_QUESTIONS):
                pitanje = PitanjeFactory(kviz=kviz)
      
