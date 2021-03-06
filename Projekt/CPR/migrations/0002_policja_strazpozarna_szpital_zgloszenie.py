# Generated by Django 3.1.3 on 2021-02-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policja',
            fields=[
                ('idPolicja', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('Nazwa', models.CharField(max_length=45)),
                ('Adres', models.CharField(max_length=45)),
                ('WolnyPojazd', models.CharField(max_length=45)),
                ('LokalizacjaPojazdu', models.CharField(max_length=45)),
                ('WolneCele', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='StrazPozarna',
            fields=[
                ('idSzpital', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('Nazwa', models.CharField(max_length=45)),
                ('Adres', models.CharField(max_length=45)),
                ('WolnyWoz', models.IntegerField(max_length=45)),
                ('WolniPracownicy', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Szpital',
            fields=[
                ('idSzpital', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('Nazwa', models.CharField(max_length=45)),
                ('Adres', models.CharField(max_length=45)),
                ('LozkoOperacyjne', models.CharField(max_length=45)),
                ('WolneMiejsca', models.IntegerField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Zgloszenie',
            fields=[
                ('idZgloszenie', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('Imie', models.CharField(max_length=45)),
                ('Nazwisko', models.CharField(max_length=45)),
                ('Miejsce', models.CharField(max_length=45)),
                ('Adres', models.CharField(max_length=45)),
                ('nrTel', models.IntegerField(max_length=9)),
                ('OpisZdarzenia', models.CharField(max_length=45)),
                ('IloscPoszkodowanych', models.CharField(max_length=45)),
                ('PoleconeCzynnosci', models.CharField(max_length=45)),
                ('CzasZgloszenia', models.CharField(max_length=45)),
            ],
        ),
    ]
