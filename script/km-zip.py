#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

vendor=input("Вендор: ") or "Konica Minolta"; vendor=str(vendor)
category=input("id Категории: ") or "CATEGORY"; category=str(category)
# type_product=input("Тип продукта: ") or "TYPE_PRODUCT"; type_product=str(type_product)

int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "KonicaMinolta"

print(counter)

raw_product = open('raw_product.csv', 'r+')
sorted_product=open('sorted_product.csv', 'w')
sorted_product_long=open('long_sorted_product.csv', 'w')

data = list(set(raw_product.readlines()))

sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')
for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	name=i[2]
	vendor_code=i[0]
	specifications=''
	slug=slugify(name+'-'+vendor_code)
	# расчет стоимости 
	price=i[6]; price=str(price); price=price.replace(",",".");
	available, stock = "1", "1"
	if 'Блок передавання зображення' in i[2]:
		type_product ='Блок'
	elif 'Тонер' in i[2]:
		type_product = 'Тонер-катридж'
	elif 'Фотоциліндр' in i[2]:
		type_product = 'Фотобарабан'
	elif 'Девелопер' in i[2]:
		type_product = 'Девелопер'
	elif 'Модуль формув. зображ' in i[2]:
		type_product = 'Блок'
	else:
		type_product = 'ЗИП'

	if len(i[1]) <= 390:
		sorted_product.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+specifications+','+type_product+','+price+','+stock+','+available+'\n')
		counter+=1
	elif len(i[1]) > 390:
		sorted_product_long.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+specifications+','+type_product+','+slug+','+price+','+stock+','+available+'\n')
		counter+=1

print(counter)

out_counter = open('counter_id.pkl', 'wb')
pickle.dump(counter, out_counter)
out_counter.close()
