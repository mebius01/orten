# Generated by Django 2.1.4 on 2019-02-24 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_auto_20190224_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polygraphy',
            name='slug',
            field=models.CharField(default='True', max_length=400),
        ),
    ]
