# Generated by Django 2.1.4 on 2019-06-28 17:13

import ckeditor.fields
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatpages', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('name_ru', models.CharField(db_index=True, max_length=200, null=True, unique=True)),
                ('name_uk', models.CharField(db_index=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category/')),
                ('description', models.TextField(blank=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.Category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('tree_id', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Polygraphy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='True', max_length=400)),
                ('image', models.ImageField(blank=True, upload_to='polygraphy/')),
                ('description', models.TextField(blank=True)),
                ('keywords', models.TextField(blank=True, help_text='Ключивые слова')),
                ('flatpage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flatpages.FlatPage')),
            ],
            options={
                'verbose_name': 'Полиграфия',
                'verbose_name_plural': 'Полиграфия',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Название товара', max_length=400)),
                ('name_ru', models.CharField(db_index=True, help_text='Название товара', max_length=400, null=True)),
                ('name_uk', models.CharField(db_index=True, help_text='Название товара', max_length=400, null=True)),
                ('slug', models.SlugField(max_length=400)),
                ('provider', models.CharField(help_text='Поставщик', max_length=20)),
                ('vendor_code', models.CharField(help_text='Артикул, парт номер', max_length=200, unique=True)),
                ('vendor', models.CharField(blank=True, help_text='Производитель', max_length=200)),
                ('type_product', models.CharField(blank=True, help_text='Тип товара', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='product/')),
                ('format_fild', models.CharField(blank=True, choices=[('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('A8', 'A8'), ('A9', 'A9'), ('A10', 'A10')], help_text='A3,A4', max_length=50)),
                ('color_fild', models.CharField(blank=True, choices=[('BW', 'BW'), ('Color', 'Color')], help_text='BW, Color', max_length=50)),
                ('specifications', ckeditor.fields.RichTextField(blank=True, help_text='Характеристики товара')),
                ('specifications_ru', ckeditor.fields.RichTextField(blank=True, help_text='Характеристики товара', null=True)),
                ('specifications_uk', ckeditor.fields.RichTextField(blank=True, help_text='Характеристики товара', null=True)),
                ('description', models.TextField(blank=True, help_text='Описание товара')),
                ('price', models.DecimalField(blank=True, decimal_places=2, help_text='Цена входящая', max_digits=10)),
                ('stock', models.PositiveIntegerField(blank=True, default=1, help_text='Остатоки')),
                ('available', models.BooleanField(default=True, help_text='Доступен ли к заказу')),
                ('start_action', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_action', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('action', models.BooleanField(default=False, help_text='Акции')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), help_text='Цена со скидкой', max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, help_text='дата обновления')),
                ('accessories', models.ManyToManyField(blank=True, editable=False, related_name='_product_accessories_+', to='shop.Product')),
                ('category', models.ForeignKey(help_text='Каталог товара (расходные материалы, компьютеры и комплетующие и т д)', on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.Category')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='Список тегов, разделенных запятыми', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=400)),
                ('name_ru', models.CharField(db_index=True, max_length=400, null=True)),
                ('name_uk', models.CharField(db_index=True, max_length=400, null=True)),
                ('slug', models.SlugField(max_length=400)),
                ('vendor_code', models.CharField(blank=True, max_length=200)),
                ('vendor', models.CharField(blank=True, help_text='Производитель', max_length=200)),
                ('vendor_model', models.CharField(blank=True, help_text='Модель', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='service/')),
                ('description', models.TextField(blank=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, help_text='Ключивые слова')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('accessories', models.ManyToManyField(blank=True, editable=False, to='shop.Product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='shop.Category')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='services',
            index_together={('id', 'slug')},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'slug')},
        ),
    ]
