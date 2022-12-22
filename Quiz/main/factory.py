import factory
from factory.django import DjangoModelFactory

from main.models import *


class KategorijaFactory(DjangoModelFactory):
    class Meta:
        model = Kategorija
    nazivKategorije = factory.Faker('word')


class KvizFactory(DjangoModelFactory):
    class Meta:
        model = Kviz
    
    naziv = factory.Faker('sentence', nb_words=7)
    opisKviza = factory.Faker('sentence', nb_words=25)

    @factory.post_generation
    def kategorije(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for kategorija in extracted:
                self.kategorija.add(kategorija)


class OpisPitanjaFactory(DjangoModelFactory):
    class Meta:
        model = OpisPitanja

    tekst = factory.Faker('sentence')


class PitanjeFactory(DjangoModelFactory):
    class Meta:
        model = Pitanje
    
    kviz = factory.SubFactory(KvizFactory)
    naziv = factory.Faker('sentence')
    opis = factory.SubFactory(OpisPitanjaFactory)
    odgovor1 = factory.Faker('word')
    odgovor2 = factory.Faker('word')
    odgovor3 = factory.Faker('word')
    odgovor4 = factory.Faker('word')
    tocan = factory.Faker('random_int',min=1,max=4)
    savjet = factory.Faker('sentence')


    