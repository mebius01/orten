#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from slugify import slugify
# import wget
import pandas as pd
import json

 #'cw' 'softcom' 'baden' 'megatrade' 'ecko'
prod_r=["Код товара", "Розничная"]; prov='baden'

raw_product = pd.read_excel('xlsx/'+prov+'.xls')
c=0
with open('json/'+prov+'.json') as json_file:
	data = json.load(json_file)
	# while c < len(raw_product):
	# 	try:

	# print(data[0].get('id'))
	while c < len(raw_product):
		# try:
		for i in data:
			if str(raw_product.iloc[c, 0]).split('.')[0] == i.get('vendor_code'):
				print(i.get('vendor_code'), i.get('name'), i.get('price'))
				i.update({'price': raw_product.iloc[c, 3]})
				print(i.get('vendor_code'), i.get('name'), i.get('price'))
			# elif str(raw_product.iloc[c, 0]).split('.')[0] != i.get('vendor_code'):
			# 	print('Vendor code not in BD', str(raw_product.iloc[c, 0]).split('.')[0])
		c+=1

# raw_product = raw_product.dropna(subset=prod_r)
# print(raw_product)

# while c < len(raw_product):
# 	try:

# vendor_code=str(raw_product.iloc[1, 0]).split('.')[0]
# print(vendor_code)

# db_product = Product.objects.filter(provider=prov) # Получить queryset
# csv_header = 'id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n'
# product_file_in_db=open('csv/sorted_product_in_db_'+prov+'.csv', 'w')
# product_file_not_in_db=open('csv/sorted_product_not_in_db_'+prov+'.csv', 'w')
# backup = open('csv/backup_'+prov+'.csv', 'w')
# backup.write(csv_header)
# product_file_in_db.write(csv_header)
# product_file_not_in_db.write(csv_header)

# def baden(rawproduct,dbproduct, productfileindb, productfilenotindb,id_t,prod_ex):
# 	rawproduct = rawproduct.dropna(subset=prod_ex) # Если один из этих столбцов имет NaN строка удаляется
# 	c=0
# 	while c < len(rawproduct):
# 		try:
# 			p = dbproduct.get(vendor_code=str(rawproduct.iloc[c, 0]).split('.')[0]) # Попытаться получить объект по vender_code
# 			if str(rawproduct.iloc[c, 4]) == "Есть":
# 				id_product=str(p.id)
# 				category=str(p.category.id)
# 				type_product=p.type_product
# 				name=str(p.name);name='"'+name.replace(',', '').replace('"','')+'"'
# 				vendor='"'+p.vendor+'"'
# 				vendor_code='"'+p.vendor_code+'"'
# 				slug=p.slug
# 				price=Create_price_b(p.price, rawproduct.iloc[c, 3])
# 				provider=p.provider
# 				available, stock = "1", "1"
# 				productfileindb.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
# 				print(rawproduct.iloc[c, 4])
# 		except Product.DoesNotExist: # Если объеки отсутсвует в БД формируем файл для импорта
# 			try:
# 				# r = rawproduct.iloc[c, :]
# 				if str(rawproduct.iloc[c, 4]) == "Есть":
# 					id_t+=1
# 					id_product=str(id_t)
# 					category="CATEGORY"
# 					name=rawproduct.iloc[c, 1];name='"'+name.replace(',', '').replace('"','')+'"'
# 					type_product="TYPE_PRODUCT"
# 					vendor = "VENDOR"
# 					vendor_code=rawproduct.iloc[c, 0];vendor_code=str(vendor_code).split('.')[0]
# 					slug=slugify(name+'-'+vendor_code)
# 					price=str(rawproduct.iloc[c, 3]);price=price.replace(",",".")
# 					provider=prov
# 					available, stock = "1", "1"
# 					productfilenotindb.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
# 			except IndexError:
# 				pass
# 		c+=1

# baden(raw_product,db_product,product_file_in_db,product_file_not_in_db,itd,prod_r)