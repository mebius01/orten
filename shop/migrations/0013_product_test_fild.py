# Generated by Django 2.1.4 on 2019-02-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_product_test_fild'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test_fild',
            field=models.CharField(blank=True, help_text='Тстовое поле на ошибку', max_length=200),
        ),
    ]
