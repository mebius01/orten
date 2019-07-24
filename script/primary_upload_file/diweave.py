#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify import slugify
import datetime 

price_file = open('diweave.csv', 'r')
product_file=open('product_diweave.csv', 'w')
data = price_file.readlines()
counter=3
for i in data:
	i=str(i).split(';')
	price=((float(i[4])*0.25)+float(i[4]))*28
	product_file.writelines(str(counter)+',72,'+i[3]+','+i[0]+','+i[1]+','+slugify(i[3])+','+str(round(price, 1))+',1'+',1'+'\n')
	counter+=1

"""
id,category,name,vendor_code,vendor,slug,price,stock,available

a = ((self.price_purchase*self.interest)+self.price_purchase)*rates_usd

#~ 0 M1 (VS17337)
#~ 1 ViewSonic
#~ 2 766907000658
#~ 3 "Проектор ультрамобільний ViewSonic M1 (VS17337) LED, WVGA 854x480, яркость-250., контраст-120000:1, HDMI / HDCPx1, Micro SD (32 Гб, SDHC), USB тип С, USB тип А, інтегрований акумулятор та пам""ять - 64 Гб, зручна підставка/кришка об'єктива, поворот 360 град., кубічний динамік 2 шт. по 3Вт, 146х126х40 мм,75 кг, колір - чорний/срібло"
#~ 4 9439,98
#~ 5 10999,08
#~ 6 8528610000
#~ 7 N


Компьютерная и офисная техника	66	kompyuternaya-i-ofisnaya-tehnika
	Акустика, наушники	72	akustika-naushniki
	Внешние жесткие диски	70	vneshnie-zhestkie-diski
	ИБП и аккумуляторы	75	ibp-i-akkumulyatory
	Кабеля, переходники, батарейки, диски, мелочь	76	kabelya-perehodniki-raznaya-meloch
	Карты памяти и флешки	68	karty-pamyati-i-fleshki
	Комплектующие	67	komplektuyushie
	Манипуляторы и мультимедиа	71	manipulyatory-i-multimedia
	Принтеры и МФУ	73	printery-i-mfu
	Проекторы и все для них	74	proektory-i-vse-dlya-nih
	Сетевое оборудование	77	setevoe-oborudovanie
	Софт	69	soft
	Телефония	78	telefoniya



	product_file.writelines(str(counter)+',72,'+i[3]+','+','+i[0]+','+i[1]+','+','+slugify(i[3])+','+','+','+','+i[4]+',0.15'+',1'+',1,'+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+','+','+'\n')
id,category,name,accessories,vendor_code,vendor,type_product,slug,image,keywords,description,price,interest,stock,available,created,updated,tags

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



Эта строка:
id,category,name,saler,vendor_code,vendor,type_product,slug,image,keywords,description,currency,price_purchase,interest,stock,available,created,updated
Всегда первая
Если id в product_diweave.csv == id в BD строка перезапишет
name не должно привышать 400 символов включая пробелы,
slug не должен привышать 400 символов включая пробелы,
created должно быть, если товар новый, или ошибка InvalidDimensions
price_purchase не должно содержать запятые 9439,98, ТОЛЬКО точку 9439.98!



#~ id,category,name,saler,vendor_code,vendor,type_product,slug,image,keywords,description,currency,price_purchase,interest,stock,available,created,updated
#~ 8,6,Акустична колонка ACME PS101 Portable Bluetooth speaker,baden,4770070879474,ACME,,akustichna-kolonka-acme-ps101-portable-bluetooth-speaker,,,,uah,3.84,0.15,1,1,,
#~ 9,6,Акустична колонка ACME PS303 Portable Bluetooth speaker,baden,4770070879498,ACME,,akustichna-kolonka-acme-ps303-portable-bluetooth-speaker,,,,uah,12.69,0.15,1,1,2019-01-06 23:09:10,
#~ 10,6,Акустична колонка ACME PS407 Bluetooth Outdoor speaker,baden,4770070879993,ACME,,akustichna-kolonka-acme-ps407-bluetooth-outdoor-speaker,,,,uah,11.59,0.15,1,1,2019-01-06 23:09:10,
#~ 11,6,Акустична колонка ACME PS408 Bluetooth Outdoor speaker,baden,4770070880005,ACME,,akustichna-kolonka-acme-ps408-bluetooth-outdoor-speaker,,,,uah,14.75,0.15,1,1,,


16385 позиций
"""
