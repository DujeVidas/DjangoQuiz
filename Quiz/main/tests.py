from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from main.views import KategorijeList, KvizoviList, PitanjaList, OpisiList, index
from main.models import Kategorija, Kviz, OpisPitanja, Pitanje


class TestUrls(SimpleTestCase):

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

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('main:index')
        self.quiz = reverse('main:kvizovi')
        self.category = reverse('main:kategorije')
        self.description = reverse('main:opisi')
        self.question = reverse('main:pitanja')


    def test_project_index_GET(self):
        client = Client()

        response = client.get(self.index)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

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


class Testmodels(TestCase):

    def setUp(self):
        self.category1 = Kategorija.objects.create(
            nazivKategorije = 'Test-Naziv'
        )

        self.quiz1 = Kviz.objects.create(
            naziv = 'Test-Kviz',
            opisKviza = 'Test opis kviza',
        )
        self.quiz1.kategorija.add(Kategorija.objects.get(id=1))

        self.description1 = OpisPitanja.objects.create(
            tekst = 'Random Test'
        )

        self.question1 = Pitanje.objects.create(
            kviz = self.quiz1,
            naziv = 'Test-Pitanje',
            opis = self.description1,
            odgovor1 = 'Test Odgovor1',
            odgovor2 = 'Test Odgovor2',
            odgovor3 = 'Test Odgovor3',
            odgovor4 = 'Test Odgovor4',
            tocan = 123,
            savjet = 'Test Savjet'
        )

    def test_category(self):
        self.assertEquals(self.category1.nazivKategorije, "Test-Naziv")

    def test_quiz(self):
        self.assertEquals(self.quiz1.naziv,"Test-Kviz")
    
    def test_description(self):
        self.assertEquals(self.description1.tekst,"Random Test")
    
    def test_question(self):
        self.assertEquals(self.question1.naziv,"Test-Pitanje")