#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

vendor=input("Вендор: ") or "Ricoh"; vendor=str(vendor)
category=input("id Категории: ") or "CATEGORY"; category=str(category)
type_product=input("Тип продукта: ") or "TYPE_PRODUCT"; type_product=str(type_product)

int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "megatrade"

print(counter)

price_file = open('raw_product.csv', 'r')
product_file=open('sorted_product.csv', 'w')
product_file_long=open('long_sorted_product.csv', 'w')
data = price_file.readlines()

product_file.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')

for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	name=i[2]
	vendor_code=i[1]
	slug=slugify(name+'-'+vendor_code) #name + vendor_code
	# расчет стоимости 
	price=i[5]
	price=(float(price.replace(",","."))*28); price=format(price, '.2f'); price=str(price)
	available, stock = "1", "1"
	if i[3] == '"Під замовлення"':
		available, stock = "0", "0"
	elif i[3] == '"В наявності"':
		available, stock = "1", "1"
	else:
		available, stock = "0", "0"
	
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