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

prov='ecko'

raw_product = pd.read_excel('work_price/'+prov+'.xlsx')
db_product = Product.objects.filter(provider=prov)
c=0
raw_product = raw_product.dropna(subset=["Адрес изображения"])
jpg_dir = os.path.join(settings.BASE_DIR, 'media', 'product')
while c < len(raw_product):
	try:
		p = db_product.get(vendor_code=str(raw_product.iloc[c, 0]))
		url = str(raw_product.iloc[c, 10])
		# filename = wget.download(url, jpg_dir)
		# os.rename(filename, jpg_dir+"/"+slugify(str(raw_product.iloc[c, 0]))+'.jpg')
		p.image = 'product/'+slugify(str(raw_product.iloc[c, 0]))+'.jpg'
		p.save()
	except Product.DoesNotExist:
		pass
	c+=1