# Generated by Django 2.1.4 on 2019-02-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190131_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='accessories',
            field=models.ManyToManyField(blank=True, related_name='_services_accessories_+', to='shop.Services'),
        ),
    ]
