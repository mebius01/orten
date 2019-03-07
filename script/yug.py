#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

# category=input("id Категории: ") or "CATEGORY"; category=str(category)
type_product=input("Тип продукта: ") or "Компьютерные комплектующие"; type_product=str(type_product)

int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "yug"

print(counter)

price_file = open('raw_product.csv', 'r')
product_file=open('sorted_product.csv', 'w')
product_file_long=open('long_sorted_product.csv', 'w')
data = price_file.readlines()
product_file.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')

for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	if i[0] == '"HDD накопичувачі"':
		category='171'
	elif i[0] == '"Блоки живлення"':
		category='172'
	elif i[0] == '"Відеокарти"':
		category='173'
	elif i[0] == '"Корпуса для PC та HDD"':
		category='174'
	elif i[0] == '"Материнські плати"':
		category='175'
	elif i[0] == '"ОЗП"':
		category='176'
	elif i[0] == '"Процесори"':
		category='177'
	elif 'TFT Монітори' in i[0]:
		category='178'
	elif 'Ноутбуки від' in i[0]:
		category='179'
	name=i[4]
	vendor=i[1]
	vendor_code=i[3]
	slug=slugify(name+'-'+vendor_code)
	price=str(i[7]); price=price.replace(",","."); price=str(price)
	if i[5] == '"Нет"':
		available, stock = "0", "0"
	elif i[5] == '"Есть"':
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