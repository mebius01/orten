#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wget
import sys, os, django
import pandas as pd
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orten.settings")
sys.path.append("/home/iv/project/virtshop/orten") #here store is root folder(means parent).
django.setup()

from orten import settings
from django.db.models import Q
from shop.models import Product, Rates, Category
from decimal import Decimal
from slugify import slugify

old_rates = Rates.objects.latest('created')

new_rates_usd=input("Текущий курс USD. Вводить число с плавающей точкой! Пример 28.03: ")
new_rates_usd=Decimal(new_rates_usd)
new_rates_eur=input("Текущий курс EUR. Вводить число с плавающей точкой! Пример 29.23: ")
new_rates_eur=Decimal(new_rates_eur)
# print(new_rates_eur, new_rates_usd) # 29 28

product_usd = Product.objects.filter(
									Q(provider='cw') |
									Q(provider='ecko') |
									Q(provider='megatrade') |
									Q(provider='printsys') |
									Q(provider='softcom')
									)
product_eur = Product.objects.filter(provider='KonicaMinolta')

for i in product_eur:
	i.price=round(((i.price/old_rates.eur)*new_rates_eur), 2)
	i.save()
for i in product_usd:
	i.price=round(((i.price/old_rates.usd)*new_rates_usd), 2)
	i.save()

new_rates = Rates.objects.create(usd=new_rates_usd, eur=new_rates_eur)
new_rates.save()