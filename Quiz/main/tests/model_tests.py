from django.test import TestCase
from main.models import *




class Testmodels(TestCase):

    def setUp(self):
        self.kategorija = Kategorija.objects.create(nazivKategorije='Kategorija 1')
        self.kviz = Kviz.objects.create(naziv='Kviz 1', opisKviza='Opis kviza',)
        self.pitanje = Pitanje.objects.create(
            kviz=self.kviz,
            naziv='Pitanje 1',
            opis=OpisPitanja.objects.create(tekst='Opis pitanja'),
            odgovor1='Odgovor 1',
            odgovor2='Odgovor 2',
            odgovor3='Odgovor 3',
            odgovor4='Odgovor 4',
            tocan=1,
            savjet='Savjet'
        )
        self.opis_pitanja = OpisPitanja.objects.create(tekst='Opis pitanja')

    def test_kategorija_str_method(self):
        self.assertEqual(str(self.kategorija), 'Kategorija 1')

    def test_kviz_str_method(self):
        self.assertEqual(str(self.kviz), 'Kviz 1')

    def test_pitanje_str_method(self):
        self.assertEqual(str(self.pitanje), 'Pitanje 1')

    def test_opis_pitanja_str_method(self):
        self.assertEqual(str(self.opis_pitanja), 'Opis pitanja')