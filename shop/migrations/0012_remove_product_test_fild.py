# Generated by Django 2.1.4 on 2019-02-14 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_test_fild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test_fild',
        ),
    ]