import datetime
# Create your models here.
from django.db import models
from django.utils import timezone

#Edit it with sql CREATE TABLE QUERIES
#question_text - kolumna
#klasa - tabela


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Zgloszenie(models.Model):
    idZgloszenie = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Miejsce = models.CharField(max_length=45)
    Adres = models.CharField(max_length=45)
    nrTel = models.IntegerField()
    OpisZdarzenia = models.CharField(max_length=45)
    IloscPoszkodowanych = models.CharField(max_length=45)
    PoleconeCzynnosci = models.CharField(max_length=45)
    CzasZgloszenia = models.CharField(max_length=45)


class Policja(models.Model):
    idPolicja = models.IntegerField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Adres = models.CharField(max_length=45)
    WolnyPojazd = models.CharField(max_length=45)
    LokalizacjaPojazdu = models.CharField(max_length=45)
    WolneCele = models.CharField(max_length=45)


class Szpital(models.Model):
    idSzpital = models.IntegerField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Adres = models.CharField(max_length=45)
    LozkoOperacyjne = models.CharField(max_length=45)
    WolneMiejsca = models.IntegerField()


class StrazPozarna(models.Model):
    idSzpital = models.IntegerField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Adres = models.CharField(max_length=45)
    WolnyWoz = models.IntegerField()
    WolniPracownicy = models.CharField(max_length=45)





