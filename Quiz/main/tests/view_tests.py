from django.test import TestCase, Client
from django.urls import reverse
from main.models import *




class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.kategorija = Kategorija.objects.create(nazivKategorije='test')
        self.kviz = Kviz.objects.create(naziv='test', opisKviza='test')
        self.opis = OpisPitanja.objects.create(tekst='test')
        self.pitanje = Pitanje.objects.create(naziv='test', tocan=1, kviz=self.kviz, opis=self.opis)


        self.index = reverse('main:index')
        self.quiz = reverse('main:kvizovi')
        self.category = reverse('main:kategorije')
        self.description = reverse('main:opisi')
        self.question = reverse('main:pitanja')
        self.create_category = reverse('main:create_kategorija')
        self.create_quiz = reverse('main:create_kviz')
        self.create_question = reverse('main:create_pitanje')
        self.create_desc = reverse('main:create_opis')

        self.update_category = reverse('main:update_kategorija',args=[self.kategorija.pk])
        self.update_quiz = reverse('main:update_kviz',args=[self.kviz.pk])
        self.update_desc = reverse('main:update_opis',args=[self.opis.pk])
        self.update_question = reverse('main:update_pitanje',args=[self.pitanje.pk])

        self.delete_category = reverse('main:delete_kategorija',args=[self.kategorija.pk])
        self.delete_quiz = reverse('main:delete_kviz',args=[self.kviz.pk])
        self.delete_desc = reverse('main:delete_opis',args=[self.opis.pk])
        self.delete_question = reverse('main:delete_pitanje',args=[self.pitanje.pk])



    def test_project_index_GET(self):
        client = Client()

        response = client.get(self.index)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_project_quiz_GET(self):
        client = Client()

        response = client.get(self.quiz)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kviz_list.html')
    
    def test_project_category_GET(self):
        client = Client()

        response = client.get(self.category)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kategorija_list.html')
    
    def test_project_description_GET(self):
        client = Client()

        response = client.get(self.description)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/opispitanja_list.html')
    
    def test_project_question_GET(self):
        client = Client()

        response = client.get(self.question)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/pitanje_list.html')

    #Create

    def test_project_category_create_GET(self):
        client = Client()

        response = client.get(self.create_category)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kategorija_form.html')
    
    def test_project_quiz_create_GET(self):
        client = Client()

        response = client.get(self.create_quiz)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kviz_form.html')
    
    def test_project_question_create_GET(self):
        client = Client()

        response = client.get(self.create_question)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/pitanje_form.html')
    
    def test_project_desc_create_GET(self):
        client = Client()

        response = client.get(self.create_desc)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/opispitanja_form.html')
    
    #Update

    def test_project_category_update_GET(self):
        client = Client()

        response = client.get(self.update_category)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kategorija_form.html')
    
    def test_project_quiz_update_GET(self):
        client = Client()

        response = client.get(self.update_quiz)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kviz_form.html')

    def test_project_desc_update_GET(self):
        client = Client()

        response = client.get(self.update_desc)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/opispitanja_form.html')
    
    def test_project_question_update_GET(self):
        client = Client()

        response = client.get(self.update_question)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/pitanje_form.html')
    
    #Delete

    def test_project_category_delete_GET(self):
        client = Client()

        response = client.get(self.delete_category)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kategorija_delete.html')
    
    def test_project_quiz_delete_GET(self):
        client = Client()

        response = client.get(self.delete_quiz)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kviz_delete.html')

    def test_project_desc_delete_GET(self):
        client = Client()

        response = client.get(self.delete_desc)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/opispitanja_delete.html')
    
    def test_project_question_delete_GET(self):
        client = Client()

        response = client.get(self.delete_question)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/pitanje_delete.html')