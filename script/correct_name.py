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
backup = open('backup_'+prov+'.csv', 'w')
db_product = Product.objects.filter(provider=prov)
c=0

for i in db_product: #backUp
	id_product=str(i.id)
	category=str(i.category.id)
	type_product=i.type_product
	name=str(i.name);name='"'+name.replace(',', '').replace('"','')+'"'
	vendor='"'+i.vendor+'"'
	vendor_code='"'+i.vendor_code+'"'
	slug=i.slug
	price=str(i.price)
	provider=i.provider
	available=str(i.available) 
	stock=str(i.stock)
	backup.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')

for i in db_product:
	list_name=str(i.name).split("/")
	new_name=''
	for l in list_name:
		new_name=new_name+l.strip()+"/ "
		i.name, i.name_ru=new_name, new_name
		i.save()
		print(i.name, i.name_ru)