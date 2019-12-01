#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from slugify import slugify
import pandas as pd
import json

 #'cw' 'softcom' 'baden' 'megatrade' 'ecko'
prod_r=["Код товара", "Розничная"]; prov='baden'

csv_header = 'id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n'
product_file_in_db=open('csv/sorted_product_in_db_'+prov+'.csv', 'w')
product_file_not_in_db=open('csv/sorted_product_not_in_db_'+prov+'.csv', 'w')
backup = open('csv/backup_'+prov+'.csv', 'w')
product_file_not_in_db.write(csv_header)

raw_product = pd.read_excel('xlsx/'+prov+'.xls')
# 0 Удалить все ненужные строки. Нужные строки определаются prov_r
raw_product = raw_product.dropna(subset=prod_r)
c=0
id_t=14918
data_list={}
a, b = 0, 0

# 1 Открыть файл экспорта baden.json для чтения
with open('json/'+prov+'.json') as json_file:
	data = json.load(json_file)
# 2 Поля available и stock обнулить'
	for i in data:
		i.update({'available': '0'})
		i.update({'stock': '0'})
	print('all products = available 0 stock 0')
# 3 Формируем данные вида 235435: {'id': 4005, 'category': 62, 'name': 'Кольцо ...} 235435 <-vendor_code
	for i in data:
		data_list[i.get('vendor_code')]=i
# 4 В цикле пытаемся получить словарь по ключу '235435'
# Если ключ есть обновляем существующие данные
	while c < len(raw_product):
		try:
			vendor_code_key = data_list.pop(str(raw_product.iloc[c, 0]).split('.')[0])
			vendor_code_key.update({'price': str(round(float(raw_product.iloc[c, 3]), 2))})
			vendor_code_key.update({'available': '1'})
			vendor_code_key.update({'stock': '1'})
			a+=1
# 5 Если ключа нет, формируем новый файл для импорта с новыми товарами
		except KeyError:
			try:
				data_list.pop(str(raw_product.iloc[c, 0]).split('.')[0]+'b')
			except KeyError:
				id_t+=1
				id_product=str(id_t)
				category="CATEGORY"
				name=raw_product.iloc[c, 1];name='"'+name.replace(',', '').replace('"','')+'"'
				type_product="TYPE_PRODUCT"
				vendor = "VENDOR"
				vendor_code=raw_product.iloc[c, 0];vendor_code=str(vendor_code).split('.')[0]
				slug=slugify(name+'-'+vendor_code)
				price=str(raw_product.iloc[c, 3]);price=price.replace(",",".")
				provider=prov
				available, stock = "1", "1"
				product_file_not_in_db.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
				b+=1
		c+=1
# 6 Формируем обновленный файл для экспорта baden-new.json 
with open('json/'+prov+'-new'+'.json', 'w') as outfile:
	json.dump(data, outfile)
# 7 Сколько в базе объектов сколько в новом файле
print("in db = ", a, " | ", "not in db = ", b )