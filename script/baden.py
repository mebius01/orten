#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify import slugify
import datetime 

price_file = open('baden.csv', 'r')
product_file=open('product_baden.csv', 'w')
product_file_long=open('product_baden_long.csv', 'w')
data = price_file.readlines()
counter=384
for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	category="CATEGORY_ID"
	name=i[1]
	vendor_code=i[0]
	vendor="VENDOR"
	type_product="PRODUCT_TYPE"
	slug=slugify(i[1]+'-'+i[0])
	price=str(i[3]); price=float(price.replace(",",".")); price=str(price)
	stock="1"
	available="1"
	if len(i[1]) <= 190:
		product_file.writelines(id_product+','+category+','+name+','+vendor_code+','+vendor+','+type_product+','+slug+','+price+','+stock+','+available+'\n')
		counter+=1
	elif len(i[1]) > 190:
		product_file_long.writelines(id_product+','+category+','+name+','+vendor_code+','+vendor+','+type_product+','+slug+','+price+','+stock+','+available+'\n')
		counter+=1

"""
id,category,name,vendor_code,vendor,type_product,slug,price,stock,available

20130;Ламинатор конвертный Royal Sovereign ES 1315 (А3) (шт.);2332,40;3332,00;Есть
"""