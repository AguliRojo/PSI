# Generated by Django 3.1.3 on 2021-02-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPR', '0002_policja_strazpozarna_szpital_zgloszenie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strazpozarna',
            name='WolnyWoz',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='szpital',
            name='WolneMiejsca',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='zgloszenie',
            name='nrTel',
            field=models.IntegerField(),
        ),
    ]
