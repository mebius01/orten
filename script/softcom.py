#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

# vendor=input("Вендор: ") or "VENDOR"; vendor=str(vendor)
category=input("id Категории: ") or "CATEGORY"; category=str(category)
type_product=input("Тип продукта: ") or "TYPE_PRODUCT"; type_product=str(type_product)
vendor_list=['F&D','Flyper','Genius','HQ-Tech','SVEN','GOLDEN FIELD','A4-Tech','Gemix','GRESSO','Logitech','SOMIC','SONY','Brother',
			'Canon','HP','Epson','LogicPower','D-Link','Dynamode','TP-Link','Mercusys','ASUS','TENDA','GEMIX','Ritar','Frime','Must','SUMRY',
			'MERLION','FrimeCom','Samsung','GOODRAM','Team','TRANSCEND','Kingston','Corsair','STEELSERIES','Rapoo','Logitech','ARESZE',
			]
type_product_list=['Клавиатура','Мышь']
int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "softcom"

print(counter)

raw_product = open('raw_product.csv', 'r')
sorted_product=open('sorted_product.csv', 'w')

data = list(set(raw_product.readlines()))

sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')
for i in data:
	i=str(i).split(';')
	if i[6]=='':
		del i
	else:
		# print(i)
		id_product=str(counter)
		name=i[4]
		vendor_code=i[2]
		specifications=''
		slug=slugify(name+'-'+vendor_code)
		price=i[6]; price=((float(price.replace(",","."))*0.15)+float(price.replace(",",".")))*28; price=format(price, '.2f'); price=str(price)
		available, stock = "1", "1"
		for v in vendor_list:
			if v.lower() in name.lower():
				vendor = v
		if type_product == 'TYPE_PRODUCT':
			for t in type_product_list:
				if t.lower() in name.lower():
					type_product = t
		sorted_product.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+specifications+','+type_product+','+price+','+stock+','+available+'\n')
		counter+=1

print(counter)

out_counter = open('counter_id.pkl', 'wb')
pickle.dump(counter, out_counter)
out_counter.close()

	# except ValueError:

	# 	print('price=0')
	# 	if i[0] == '"05 - FLASH память"':
	# 		category = '68'
	# 		print(category)
	# 	elif i[3] == '"11 - Клавиатуры"':
	# 		category == '71'
	# 	elif i[3] == '"12 - Мыши"':
	# 		category == '71'
	# 	elif i[3] == '"14 - АКУСТИКА и НАУШНИКИ"':
	# 		category == '72'
	# 	elif i[3] == '"17 - Принтеры и МФУ"':
	# 		category == '73'
	# 	elif i[3] == '"25 - Сетевое оборудование"':
	# 		category == '77'
	# 	elif i[3] == '"23 - ИБП, Сетевые фильтры, Стабилизаторы, Батареи для ИБП"':
	# 		category == '75'
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	# elif i[3] == '':
	# 	# 	category == ''
	# 	else:
	# 		vendor = i[3].replace(' ', '')
	# 	print
