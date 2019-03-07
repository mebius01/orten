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

data = list(set(raw_product.readlines()))

sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')
for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	name=i[1]
	vendor_code=i[0]
	specifications=i[2]
	slug=slugify(name+'-'+vendor_code)
	# расчет стоимости 
	price=i[6]; price=str(price); price=price.replace(",",".");
	available, stock = "1", "1"
	sorted_product.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+specifications+','+type_product+','+price+','+stock+','+available+'\n')
	counter+=1

print(counter)

out_counter = open('counter_id.pkl', 'wb')
pickle.dump(counter, out_counter)
out_counter.close()
