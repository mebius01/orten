# Generated by Django 2.1.4 on 2019-02-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_polygraphy_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_fild',
            field=models.CharField(blank=True, choices=[('', ''), ('BW', 'BW'), ('Color', 'Color')], help_text='BW, Color', max_length=50),
        ),
    ]