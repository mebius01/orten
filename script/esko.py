#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify import slugify
# from shop.models import Product
import datetime 

price_file = open('esko.csv', 'r')
product_file=open('product_esko.csv', 'w')
data = price_file.readlines()
counter=4
for i in data:
	i=str(i).split(';')
	#~ for a in i:
	# product_file.writelines(str(counter)+',79,'+'"'+i[1]+'"'+',esko,'+i[0]+','+i[2]+','+i[3]+','+slugify(i[1])+','+','+','+',usd,'+i[5]+',0.30'+',1'+',1,'+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+','+'\n')
	print(str(counter)+',79,'+i[3]+',baden,'+i[0]+','+i[1]+','+slugify(i[3])+',products/2018/12/29/foo.jpg'+','+','+',uah,'+i[4]+',0.15'+',1'+',1,'+str(datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S"))+','+str(datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S"))+',')
	print(counter)
	counter+=1

"""
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
9 Наличие;
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
