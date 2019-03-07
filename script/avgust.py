#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

vendor=input("Вендор: ") or "August"; vendor=str(vendor)
category=input("id Категории: ") or "155"; category=str(category)
type_product=input("Тип продукта: ") or "Визиточный картон"; type_product=str(type_product)

int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "avgust"

print(counter)

price_file = open('raw_product.csv', 'r')
product_file=open('sorted_product.csv', 'w')
data = price_file.readlines()
product_file.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')

# "Tintoretto ceylon ginepro";"синий";"легкая фактура";" ";72;101;"250 г/м2";"0.182 кг";"1.51 ";"картон";"со склада"

for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	name=i[0]
	vendor_code=slugify(name+'-'+i[6])
	slug=vendor_code
	specifications ='"'+"Цвет: "+i[1][1:-1]+", "+"Фактура: "+i[2][1:-1]+'"'
	try:
		price=str(i[8][1:-2])
		price=(((float(price)*0.30)+float(price))*29.5)/9; price=format(price, '.2f'); price=str(price)
	except ValueError:
		price=str(i[8])
		price=(((float(price)*0.30)+float(price))*29.5)/9; price=format(price, '.2f'); price=str(price)
	available, stock = "1", "1"

	if len(i[1]) <= 390:
		product_file.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+specifications+','+type_product+','+price+','+stock+','+available+'\n')
		counter+=1

print(counter)

out_counter = open('counter_id.pkl', 'wb')
pickle.dump(counter, out_counter)
out_counter.close()