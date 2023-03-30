from django.test import TestCase
from django.urls import reverse, resolve
from main.views import *
from main.models import *



class TestUrls(TestCase):



    def setUp(self):
        self.kategorija = Kategorija.objects.create(nazivKategorije='test')
        self.kviz = Kviz.objects.create(naziv='test', opisKviza='test')
        self.opis = OpisPitanja.objects.create(tekst='test')
        self.pitanje = Pitanje.objects.create(naziv='test', tocan=1, kviz=self.kviz, opis=self.opis)


    def test_index_url_is_resolved(self):
        url = reverse('main:index')

        self.assertEquals(resolve(url).func, index)

    def test_category_url_is_resolved(self):
        url = reverse('main:kategorije')

        self.assertEquals(resolve(url).func.view_class, KategorijeList)

    def test_quizzes_url_is_resolved(self):
        url = reverse('main:kvizovi')

        self.assertEquals(resolve(url).func.view_class, KvizoviList)
    
    def test_questions_url_is_resolved(self):
        url = reverse('main:pitanja')

        self.assertEquals(resolve(url).func.view_class, PitanjaList)
    
    def test_description_url_is_resolved(self):
        url = reverse('main:opisi')

        self.assertEquals(resolve(url).func.view_class, OpisiList)

    #Create
    def test_create_category_url_is_resolved(self):
        url = reverse('main:create_kategorija')
        self.assertEquals(resolve(url).func,createKategorija)
    
    def test_create_quiz_url_is_resolved(self):
        url = reverse('main:create_kviz')
        self.assertEquals(resolve(url).func,createKviz)
    
    def test_create_question_url_is_resolved(self):
        url = reverse('main:create_pitanje')
        self.assertEquals(resolve(url).func,createPitanje)

    def test_create_desc_url_is_resolved(self):
        url = reverse('main:create_opis')
        self.assertEquals(resolve(url).func,createOpis)
    
    #Update

    
    def test_update_category_url_is_resolved(self):

        url = reverse('main:update_kategorija', kwargs={'pk': self.kategorija.pk})
        self.assertEquals(resolve(url).func,updateKategorija)
    
    def test_update_quiz_url_is_resolved(self):

        url = reverse('main:update_kviz',kwargs={'pk': self.kviz.pk})
        self.assertEquals(resolve(url).func,updateKviz)
    
    def test_update_question_url_is_resolved(self):
        url = reverse('main:update_pitanje',kwargs={'pk': self.pitanje.pk})
        self.assertEquals(resolve(url).func,updatePitanje)
    
    def test_update_desc_url_is_resolved(self):
        url = reverse('main:update_opis',kwargs={'pk': self.opis.pk})
        self.assertEquals(resolve(url).func,updateOpis)
    
    #Delete

    def test_delete_category_url_is_resolved(self):

        url = reverse('main:delete_kategorija', kwargs={'pk': self.kategorija.pk})
        self.assertEquals(resolve(url).func,deleteKategorija)
    
    def test_delete_quiz_url_is_resolved(self):

        url = reverse('main:delete_kviz',kwargs={'pk': self.kviz.pk})
        self.assertEquals(resolve(url).func,deleteKviz)
    
    def test_delete_question_url_is_resolved(self):
        url = reverse('main:delete_pitanje',kwargs={'pk': self.pitanje.pk})
        self.assertEquals(resolve(url).func,deletePitanje)
    
    def test_delete_desc_url_is_resolved(self):
        url = reverse('main:delete_opis',kwargs={'pk': self.opis.pk})
        self.assertEquals(resolve(url).func,deleteOpis)
    