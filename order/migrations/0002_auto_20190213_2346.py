# Generated by Django 2.1.4 on 2019-02-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='department_np',
            field=models.CharField(max_length=300, verbose_name='НП №'),
        ),
    ]