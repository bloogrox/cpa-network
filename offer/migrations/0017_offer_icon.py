# Generated by Django 3.0.7 on 2020-07-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0016_auto_20200629_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
