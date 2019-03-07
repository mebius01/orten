#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

# vendor=input("Вендор: ") or "VENDOE"; vendor=str(vendor)
# category=input("id Категории: ") or "CATEGORY"; category=str(category)
# type_product=input("Тип продукта: ") or "TYPE_PRODUCT"; type_product=str(type_product)

int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "ecko"

print(counter)

price_file = open('raw_product.csv', 'r')
product_file=open('sorted_product.csv', 'w')
product_file_long=open('long_sorted_product.csv', 'w')
data = price_file.readlines()
product_file.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')

for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	vendor_code=i[0]
	name=i[1]
	vendor=i[2]
	if "Мастер".lower() in name.lower():
		type_product = "Мастер-пленка"
		category = '129'
	elif "Чернила".lower() in name.lower():
		type_product = "Чернила"
		category = '129'
	elif "Чип".lower() in name.lower():
		type_product = "Чипы"
		category = '128'
	elif "Вал".lower() in name.lower():
		type_product = "Вал"
		category = '128'
	elif "Термопленк".lower() in name.lower():
		category = '128'
		type_product = "ЗИП"
	elif "Картридж".lower() in name.lower():
		category = '129'
		type_product = "Картриджи"
	elif "Подшипник".lower() in name.lower():
		category = '128'
		type_product = "Подшипники"
	elif "Втулк".lower() in name.lower():
		category = '128'
		type_product = "Втулки"
	elif "Лезвие".lower() in name.lower():
		category = '128'
		type_product = "Лезвия"
	elif "Ролик".lower() in name.lower():
		type_product = "Ролики"
		category = '128'
	elif "Сепаратор".lower() in name.lower():
		type_product = "Сепараторы"
		category = '128'
	elif "Тонер-картридж".lower() in name.lower():
		category = '129'
		type_product = "Тонер-картриджи"
	elif "Девелопер".lower() in name.lower():
		category = '129'
		type_product = "Девелопер"
	elif "Фотобарабан".lower() in name.lower():
		category = '129'
		type_product = "Фотобарабаны"
	elif "Шестерн".lower() in name.lower():
		type_product = "Шестерни"
		category = '128'
	elif "Термистор".lower() or "площадка".lower() in name.lower():
		type_product = "ЗИП"
		category = '128'
	elif "Тонер".lower() in name.lower():
		category = '129'
		type_product = "Тонера" 
	elif "Блок".lower() in name.lower():
		type_product = "Блоки"
		category = '128'
	# elif "Смазка".lower() or "Спрей".lower() or "Жидкость".lower() or "Очиститель".lower() or "Присыпка".lower() or "Пудра".lower() in name.lower():
	# 	type_product = "Средства ухода"
	# 	category = '130'
	elif "Узел".lower() in name.lower():
		type_product = "Узелы"
		category = '128'
	slug=slugify(name+'-'+vendor_code)
	price=str(i[5]); price=((float(price.replace(",","."))*0.30)+float(price.replace(",",".")))*28; 
	price=format(price, '.2f')
	price=str(price)
	# if type_product == 'TYPE_PRODUCT':
	# 	for t in type_product_list:
	# 		if t.lower() in name.lower()::
	# 			type_product = t
	# если в прайсе есть то сток наличе == 1
	# if i[9] == '"Нет"':
	# 	available, stock = "0", "0"
	# elif i[9] == '"Да"':
	available, stock = "1", "1"

	if len(i[1]) <= 390:
		product_file.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
		counter+=1
	elif len(i[1]) > 390:
		product_file_long.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+slug+','+price+','+stock+','+available+'\n')
		counter+=1

print(counter)

out_counter = open('counter_id.pkl', 'wb')
pickle.dump(counter, out_counter)
out_counter.close()