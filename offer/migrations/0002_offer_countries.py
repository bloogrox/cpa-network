# Generated by Django 2.2.5 on 2019-09-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='countries',
            field=models.ManyToManyField(to='countries_plus.Country'),
        ),
    ]
