# Generated by Django 2.1.4 on 2019-01-28 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190128_1501'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='services',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='services',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
