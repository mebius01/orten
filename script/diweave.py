#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify import slugify
import datetime 

price_file = open('diweave.csv', 'r')
product_file=open('product_diweave.csv', 'w')
data = price_file.readlines()
counter=7
for i in data:
	i=str(i).split(';')
	product_file.writelines(str(counter)+',6,'+i[3]+',baden,'+i[0]+','+i[1]+','+','+slugify(i[3])+','+','+','+',uah,'+i[4]+',0.15'+',1'+',1,'+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+','+'\n')
	counter+=1


"""
#~ 0 M1 (VS17337)
#~ 1 ViewSonic
#~ 2 766907000658
#~ 3 "Проектор ультрамобільний ViewSonic M1 (VS17337) LED, WVGA 854x480, яркость-250., контраст-120000:1, HDMI / HDCPx1, Micro SD (32 Гб, SDHC), USB тип С, USB тип А, інтегрований акумулятор та пам""ять - 64 Гб, зручна підставка/кришка об'єктива, поворот 360 град., кубічний динамік 2 шт. по 3Вт, 146х126х40 мм,75 кг, колір - чорний/срібло"
#~ 4 9439,98
#~ 5 10999,08
#~ 6 8528610000
#~ 7 N


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
