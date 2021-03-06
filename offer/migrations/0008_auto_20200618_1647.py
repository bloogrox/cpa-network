# Generated by Django 2.2.6 on 2020-06-18 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_offer_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferTrafficSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed', models.BooleanField(default=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Offer')),
                ('traffic_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.TrafficSource')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='traffic_sources',
            field=models.ManyToManyField(through='offer.OfferTrafficSource', to='offer.TrafficSource'),
        ),
    ]
