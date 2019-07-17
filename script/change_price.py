#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wget
import sys, os, django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orten.settings")
sys.path.append("/home/iv/project/virtshop/orten") #here store is root folder(means parent).
django.setup()

from orten import settings
from django.db.models import Q
from shop.models import Product, Rates
from decimal import Decimal
from slugify import slugify


########## Добавления изображения ecko Рабочий код

# row_product = pd.read_excel('ecko.xlsx')
# row_product.dropna(inplace = True)

# movies = row_product[["PartNumber", "Адрес изображения"]]
# row_dict = movies.head(66).to_dict()

# list_keys = list(row_dict.get("PartNumber").keys())
# c=0
# jpg_dir = os.path.join(settings.BASE_DIR, 'media', 'product')
# db_product = Product.objects.filter(provider='ecko')

# while c < len(list_keys):
# 	for i in db_product:
# 		if i.vendor_code == row_dict.get("PartNumber").get(list_keys[c]):
# 			url = row_dict.get("Адрес изображения").get(list_keys[c])
# 			filename = wget.download(url, jpg_dir)
# 			os.rename(filename, jpg_dir+"/"+slugify(row_dict.get("PartNumber").get(list_keys[c]))+'.jpg')
# 			i.image = 'product/'+slugify(row_dict.get("PartNumber").get(list_keys[c]))+'.jpg'
# 			i.save()
# 	c+=1

##########


########## Обновление цен Рабочий код

# new_rates_usd=input("Текущий курс USD. Вводить число с плавающей точкой! Пример 28.03: ")
# new_rates_usd=Decimal(new_rates_usd)
# new_rates_eur=input("Текущий курс EUR. Вводить число с плавающей точкой! Пример 29.23: ")
# new_rates_eur=Decimal(new_rates_eur)
# print(new_rates_eur, new_rates_usd) # 29 28

# product_usd = Product.objects.filter(
# 									Q(provider='cw') |
# 									Q(provider='ecko') |
# 									Q(provider='megatrade') |
# 									Q(provider='printsys') |
# 									Q(provider='softcom')
# 									)
# product_eur = Product.objects.filter(provider='KonicaMinolta')

# for i in product_eur:
# 	i.price=round(((i.price/old_rates.eur)*new_rates_eur), 2)
# 	i.save()
# for i in product_usd:
# 	i.price=round(((i.price/old_rates.usd)*new_rates_usd), 2)
# 	i.save()

# new_rates = Rates.objects.create(usd=new_rates_usd, eur=new_rates_eur)
# new_rates.save()

##########









########## рабочий код
# old_rates = Rates.objects.latest('created')

# last_id = Product.objects.latest('id').id # последние id в BD
# raw_product = open('raw_product.csv', 'r')
# sorted_product=open('sorted_product.csv', 'a')
# db_product=open('db_product.csv', 'r+')
# sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')

# data_db = db_product.readlines()
# data_raw = raw_product.readlines()

# db_list={}
# raw_list={}


# for d in data_db:
# 	d=d.split(';')
# 	db_list[d[5][1:-1]]=d
# for r in data_raw:
# 	if str(r).split(';')[0] != '':
# 		r=r.split(';')
# 		raw_list[r[0][1:-1]]=r
##########

########## рабочий код
# for d in db_list:
# 	if d in raw_list:
# 		if db_list.get(d)[8].split(',')[0] != raw_list.get(d)[3].split(',')[0]:
# 			db_list.get(d)[3]=db_list.get(d)[3][1:-1]
# 			db_list.get(d)[4]=db_list.get(d)[4][1:-1]
# 			db_list.get(d)[5]=db_list.get(d)[5][1:-1]
# 			db_list.get(d)[6]=db_list.get(d)[6][1:-1]
# 			db_list.get(d)[7]=db_list.get(d)[7][1:-1]
# 			db_list.get(d)[8]=raw_list.get(d)[3].replace(",",".")
# 			db_list.get(d)[9]='1'
# 			db_list.get(d)[10]='1'+'\n'
# 			sorted_product.write(','.join(db_list.get(d)))
# 	if d not in raw_list:
# 		db_list.get(d)[3]=db_list.get(d)[3][1:-1]
# 		db_list.get(d)[4]=db_list.get(d)[4][1:-1]
# 		db_list.get(d)[5]=db_list.get(d)[5][1:-1]
# 		db_list.get(d)[6]=db_list.get(d)[6][1:-1]
# 		db_list.get(d)[7]=db_list.get(d)[7][1:-1]
# 		db_list.get(d)[8]=db_list.get(d)[8].replace(",",".")  #price замена , на .
# 		db_list.get(d)[9]='0'
# 		db_list.get(d)[10]='0'+'\n'
# 		sorted_product.write(','.join(db_list.get(d)))
##########

########## рабочий код
# for r in raw_list:
# 	if r not in db_list:
# 		last_id+=1
# 		id_product=str(last_id)
# 		category="60"
# 		provider="baden"
# 		vendor="TEST-vendor"
# 		type_product="TEST-type_product"
# 		name=raw_list.get(r)[1]
# 		vendor_code=raw_list.get(r)[0][1:-1]
# 		slug=slugify(name+'-'+vendor_code)
# 		price=raw_list.get(r)[3].replace(",",".")
# 		available, stock = "1", "1"
# 		sorted_product.write(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
##########



# print(raw_list.get(r), r, 'not in db_list')
# 14952,TEST-category,"Пружины пластиковые 28 мм, прозрачные (50 шт.) (уп.)",pruzhiny-plastikovye-28-mm-prozrachnye-50-sht-up-43657,baden,"43657",TEST-vendor,TEST-type_product,239,68,1,1

# "26102"
# "Держатель баннера XY2-F2 типа ""паук"" 600x1600 (пласт.крепление) (шт.)"
# 318,64
# 455,00
# "Есть"
# [1:-1]


		# print(db_list.get(d),d, 'not in raw_product') # если нет значение ("stock";"available") а файле DB_LIST выстовить в ноль
# print(raw_list.get('14050'))
# print(Product.objects.latest('id'), Product.objects.latest('id').id, type(Product.objects.latest('id').id))
# c=0
# for i in db_list:
# 	c+=1
# 	print(c)
# print(db_list)
"""
		# db_list.get(d)[2]=db_list.get(d)[2][1:-1]
		# db_list.get(d)[3]=db_list.get(d)[3][1:-1]
		# db_list.get(d)[4]=db_list.get(d)[4][1:-1]
		# db_list.get(d)[5]=db_list.get(d)[5][1:-1]
		# db_list.get(d)[6]=db_list.get(d)[6][1:-1]
		# db_list.get(d)[7]=db_list.get(d)[7][1:-1]
		# db_list.get(d)[10]=db_list.get(d)[10][1:-2]

3935 <class 'str'>0
157 <class 'str'>1
"Шредер DSB AF75" <class 'str'>2
"unichtozhitel-dokumentov-dsb-af75-sht-24330" <class 'str'>3
"baden" <class 'str'>4
"24330" <class 'str'>5
"DSB" <class 'str'>6
"Уничтожитель документов" <class 'str'>7
6860,00 <class 'str'>8
1 <class 'str'>9
"1" <class 'str'>10
"""


			# for num_db, i in enumerate(db_list.get(d)):
			# 	print(i,[num_db], db_list.get(d)[8].split(',')[0], raw_list.get(d)[3].split(',')[0])
				# print('the is befor', db_list.get(d)[8].split(',')[0], raw_list.get(d)[3].split(',')[0])
				# db_list.get(d)[num_db] = raw_list.get(d)[3]
				# print('the is after', db_list.get(d)[8].split(',')[0], raw_list.get(d)[3].split(',')[0])
		# if list(r.keys())[0] == list(d.keys())[0]:
			# print(r.get(list(r.keys())[0])[3], '---', d.get(list(d.keys())[0])[8], '\n') #price
			# print(r.get(list(r.keys())[0])[3], '---', d.get(list(d.keys())[0])[8], '\n')

# >>> a= [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
# >>> for n, i in enumerate(a):
# ...   if i == 1:
# ...      a[n] = 10
# ...
# >>> a
# [10, 2, 3, 4, 5, 10, 2, 3, 4, 5, 10]

# print(db_list[1]) #{'21767': ['14898', '47', '"Обжимное устройство для металлической пружины MC430 PLUS"', '"binder-na-metallicheskoj-pruzhiny-mc430-plus-21767"', '"baden"', '"21767"', '"lamiMARK"', '', '10360', '0', '"1"\n']}

# print(db_list[1])
# print(raw_list[1])
	# print(list({d[5][1:-1]:d}.keys())[0], {d[5][1:-1]:d}.get(list({d[5][1:-1]:d}.keys())[0]))
	# print(d[5])

	# print(str(r).split(';')[0][1:-1]) == 47602 (vendor_code)
	# print(str(r).split(';')[1][1:-1]) == 15.9 мм, черные wireMARK (10 500 петель) (боб.) (name)
	# print(str(r).split(';')[2]) == 161,28 (price PARTNER)
	# print(str(r).split(';')[3]) == 4891,32 (price RETAIL)

	# if str(r).split(';')[0] != '':
	# 	for i in data_db:
	# 		try:
	# 			if str(r).split(';')[3].split(',')[0] == str(i).split(';')[9].split(',')[0]:
	# 				# if str(r).split(';')[3].split(',')[0:-3] != str(i).split(';')[9].split(',')[0:-2]:
	# 				print(str(r).split(';')[3].split(',')[0] , str(i).split(';')[9].split(',')[0])
	# 			else:
	# 				print("False",(str(r).split(';')[3].split(',')[0] , str(i).split(';')[9].split(',')[0]))
	# 		except IndexError:
	# 			pass
	# if str(r).split(';')[0] != '':
	# 	for i in data_db:
	# 		try:
	# 			if str(i).split(';')[5][1:-1] != str(r).split(';')[0][1:-1]:
	# 				print(r, counter)
	# 				counter+=1
	# 		except IndexError:
	# 			break

# for i in data_db:
 	# print(str(i).split(';')[0]) == 2027 (id DB)
 	# print(str(i).split(';')[1]) == 59 (Category)
 	# print(str(i).split(';')[2][1:-1]) == 15.9 мм, черные wireMARK (10 500 петель) (боб.) (name)
 	# print(str(i).split(';')[3]) == "15-9-mm-chernye-wiremark-10-500-petel-bob-47602" (slug)
 	# print(str(i).split(';')[4][1:-1]) ==  baden (provider)
 	# print(str(i).split(';')[5[1:-1]]) == 47602 (vendor_code)
 	# print(str(i).split(';')[6][1:-1]) == lamiMARK (vendor)
 	# print(str(i).split(';')[7][1:-1]) == Пружины (type_roduct)
 	# print(str(i).split(';')[8]) == (specifications)
 	# print(str(i).split(';')[9]) == 161,28 (price)
	# print(str(i).split(';')[10:12]) == ['1', '"1"\n'] ("stock";"available")
	# if str(i).split(';')[0] == '4519':
	# 	print(i)