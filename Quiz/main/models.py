from django.db import models

# Create your models here.

class Kategorija(models.Model):
    nazivKategorije = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nazivKategorije


class Kviz(models.Model):
    naziv = models.CharField(max_length=100)
    opisKviza = models.CharField(max_length=255)
    kategorija = models.ManyToManyField(Kategorija)

    def __str__(self) -> str:
        return self.naziv


class Pitanje(models.Model):
    kviz = models.ForeignKey(Kviz, on_delete=models.CASCADE)
    naziv = models.CharField(max_length=50,blank=True,null=True)
    opis = models.OneToOneField('OpisPitanja', on_delete=models.CASCADE)
    odgovor1 = models.CharField(max_length=150)
    odgovor2 = models.CharField(max_length=150)
    odgovor3 = models.CharField(max_length=150)
    odgovor4 = models.CharField(max_length=150)
    tocan = models.IntegerField()
    savjet = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.naziv



class OpisPitanja(models.Model):
    tekst = models.TextField()

    def __str__(self) -> str:
        return self.tekst
