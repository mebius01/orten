#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from slugify import slugify
import datetime 

vendor_code_list=[]
price_file = open('esko.csv', 'r')
product_file=open('product_esko.csv', 'w')
product_file_long=open('product_file_long.csv', 'w')
data = price_file.readlines()
counter=56
for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	category="CATEGORY_ID"
	name=i[1]
	vendor_code=i[0]
	vendor_code_list.append(i[0])
	vendor=i[2]
	type_product=i[3]
	slug=slugify(i[1],i[0])

	# расчет стоимости 
	price=str(i[5]); price=((float(price.replace(",","."))*0.30)+float(price.replace(",",".")))*28; price=str(price)

	# если в прайсе есть сток до наличе == 1
	if i[9] == 'Нет':
		available, stock = "0", "0"
	elif i[9] == "Да":
		available, stock = "1", "1"

	if len(i[1]) <= 390:
		product_file.writelines(id_product+','+category+','+name+','+vendor_code+','+vendor+','+type_product+','+slug+','+price+','+stock+','+available+'\n')
		counter+=1
	elif len(i[1]) > 390:
		product_file_long.writelines(id_product+','+category+','+name+','+vendor_code+','+vendor+','+type_product+','+slug+','+price+','+stock+','+available+'\n')
		counter+=1
print(vendor_code_list)


	# a=str(i[5])
	# price=((float(a.replace(",","."))*0.25)+float(a.replace(",",".")))*28
	# if len(i[1]) <= 190:
	# 	product_file.writelines(str(counter)+',"CATEGORY_ID",'+i[1]+','+i[2]+','+i[2]+','+slugify(i[0])+','+str(round(price, 1))+',1'+',1'+'\n')
	# 	counter+=1
	# elif len(i[1]) > 190:
	# 	product_file_long.writelines(str(counter)+',"CATEGORY_ID",'+i[1]+','+i[2]+','+i[2]+','+slugify(i[0])+','+str(round(price, 1))+',1'+',1'+'\n')
	# 	counter+=1

# Все таки Python динамичен и выразителен. Этого у него не отнять.

# Там некоторые логические и арифметические операторы перегружены для множеств.

# Вот Ваш однострочник:

# result=list(set(Ans) & set(Word))
# Это даст пересечение обоих списков:

# ['red', 'white']
# Если нужен список уникальных элементов в объединении двух списков:

# ['red', 'white', 'green', 'blue']

# result = list(set(Ans + Word))
# Симметричная разность:

# ['green','blue']

# result=list(set(Ans) ^ set(Word))
# Обычная разность(Множество из Ans не входящее в Word):

# ['green','blue']

# result=list(set(Ans) - set(Word))
# Вариант, сохраняющий порядок с меньшим количеством конверсий типов:

# sbuf = set(Word)
# result = [x for x in Ans if x in sbuf)]


"""
id,category,name,vendor_code,vendor,type_product,slug,price,stock,available

id, str(counter)
category, 1
name, i[1]
accessories, 
saler, 'esko'
vendor_code, i[0]
vendor, i[2]
type_product, i[3]
slug,
image,
keywords,
description,
currency, 'usd'
price_purchase, i[5]
interest,
stock,
available,
created,
updated

0 PartNumber;
1 Название товара;
2 Производитель;
3 Тип;
4 "Область применения";
5 Цена;
6 Тенденция;
7 Рекоменд. цена;
8 "Мин. партия";
9 Наличие; Да Нет
10 Адрес изображения;
11 GoodsNameID

Эта строка:
id,category,name,saler,vendor_code,vendor,type_product,slug,image,keywords,description,currency,price_purchase,interest,stock,available,created,updated
Всегда первая
Если id в product_diweave.csv == id в BD строка перезапишет
name не должно привышать 400 символов включая пробелы,
slug не должен привышать 400 символов включая пробелы,
created должно быть, если товар новый, или ошибка InvalidDimensions
price_purchase не должно содержать запятые 9439,98, ТОЛЬКО точку 9439.98!


9850,1,"Фотобарабан ECKO для Samsung CLP 300/ 310 (Green color)",esko,ECKO-GMS-SS C407,ЕСКО,Фотобарабаны,fotobaraban-ecko-dlia-samsung-clp-300-310-green-color,,,,usd,21,0.30,1,1,2019-01-07 03:40:09,
9851,1,"Фотобарабан ECKO для Samsung ML 1210 (Green color)",esko,ECKO-GS-SS1210,ЕСКО,Фотобарабаны,fotobaraban-ecko-dlia-samsung-ml-1210-green-color,,,,usd,1,0.30,1,1,2019-01-07 03:40:09,
9852,1,"Фотобарабан ECKO для Samsung ML 1510/ 1710/ 1750/ SCX-4016/ 4100/ 4116/ 4200/ 4216/ 4300/ Xerox Phaser 3114/ 3115/ 3120/ 3130/ 3150/ WC 3119/ Pe16/ Pe114e/ Green",esko,ECKO-GS-SS1710,ЕСКО,Фотобарабаны,fotobaraban-ecko-dlia-samsung-ml-1510-1710-1750-scx-4016-4100-4116-4200-4216-4300-xerox-phaser-3114-3115-3120-3130-3150-wc-3119-pe16-pe114e-green,,,,usd,1,0.30,1,1,2019-01-07 03:40:09,
"""
