#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wget
import sys, os, django
import pandas as pd
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orten.settings")
sys.path.append("/home/iv/project/virtshop/orten") #here store is root folder(means parent).
django.setup()

from orten import settings
from django.db.models import Q
from shop.models import Product, Rates, Category
from decimal import Decimal
from slugify import slugify

########## Dump Product

# from django.core.management import call_command
# output = open('dump_product.json','w')
# call_command('dumpdata', 'shop.Product', format='json', indent=3, stdout=output)
# output.close()

##########

########## Обновление полей available

# e=input("ecko = 1: ")
# s=input("softcom = 2: ")
# m=input("megatrade = 3: ")
# b=input("baden = 4: ")

# e_r=["PartNumber", 
# 	"Название товара", 
# 	"Производитель", 
# 	"Тип", 
# 	"Цена", 
# 	"Наличие", 
# 	"Адрес изображения"];

# m_r=["Артикул ", 
# 	"Номенклатура", 
# 	"Залишок",
# 	"Валюта",
# 	"Стандартна роздрібна ціна",
# 	"Стандартна партнерська ціна",
# 	"Спеціальна ціна",
# 	"Опис"]

# b_r=["Код товара",
# 	"Остаток",
# 	"Наименование товаров",
# 	"Партнер",
# 	"Розничная"]


# prod_r=["Код"] # CW

prod_r = ["Номенклатура.Код", 
	"Номенклатура.Артикул ", 
	"Номенклатура", 
	"Цена", 
	"+ -"] 

prov='softcom' #'cw' 'softcom' 'baden' 'megatrade' 'ecko'

# Функция расчета цены
def Create_price(pric, rate, procent):
	pric=str(pric)
	pric=pric.replace(",",".")
	pric=Decimal(pric)*rate
	procent = Decimal(procent)*Decimal(pric)
	return str(round(pric+procent, 2))


rates = Rates.objects.latest('created')
itd=Product.objects.latest('id').id+1 # Получить последний id + 1

raw_product = pd.read_excel('work_price/'+prov+'.xlsx')
db_product = Product.objects.filter(provider=prov) # Получить queryset
csv_header = 'id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n'
product_file_in_db=open('sorted_product_in_db.csv', 'w')
product_file_not_in_db=open('sorted_product_not_in_db.csv', 'w')
backup = open('backup_'+prov+'.csv', 'w')
backup.write(csv_header)
product_file_in_db.write(csv_header)
product_file_not_in_db.write(csv_header)

for i in db_product:
	id_product=str(i.id)
	category=str(i.category.id)
	type_product=i.type_product
	name=str(i.name);name='"'+name.replace(',', '').replace('"','')+'"'
	vendor='"'+i.vendor+'"'
	vendor_code='"'+i.vendor_code+'"'
	slug=i.slug
	price=str(i.price)
	provider=i.provider
	available=str(i.available) 
	stock=str(i.stock)
	backup.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
	i.available = False
	i.stock = False
	i.save()

########## Обновление полей available softcom

def softcom(rawproduct,dbproduct, productfileindb, productfilenotindb,id_t,prod_ex):

	rawproduct = rawproduct.dropna(subset=prod_ex)

	vendor_list=['F&D','Flyper','Genius','HQ-Tech','SVEN','GOLDEN FIELD','A4-Tech','Gemix','GRESSO','Logitech','SOMIC','SONY','Brother',
			'Canon','HP','Epson','LogicPower','D-Link','Dynamode','TP-Link','Mercusys','ASUS','TENDA','GEMIX','Ritar','Frime','Must','SUMRY',
			'MERLION','FrimeCom','Samsung','GOODRAM','Team','TRANSCEND','Kingston','Corsair','STEELSERIES','Rapoo','Logitech','ARESZE',
			]
	c=0
	while c < len(rawproduct):
		try:
			p = dbproduct.get(vendor_code=str(rawproduct.iloc[c, 1])) # Попытаться получить объект по vender_code 
			# print(p, "in bd")
			id_product=str(p.id)
			category=str(p.category.id)
			type_product=p.type_product
			name=str(p.name);name='"'+name.replace(',', '').replace('"','')+'"'
			vendor='"'+p.vendor+'"'
			vendor_code='"'+p.vendor_code+'"'
			slug=p.slug
			price=str(p.price)
			provider=p.provider
			available, stock = "1", "1"
			productfileindb.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
			# p.available = True; p.save() # Присвоить значение True если в прайсе "В наявності"
		except Product.DoesNotExist: # Если объеки отсутсвует в БД формируем файл для импорта
			try:
	# 			# Если один из этих столбцов имет NaN строка удаляется
				# r = rawproduct.dropna(subset=["Номенклатура.Артикул "]).iloc[c, :]
				id_t+=1
				id_product=str(id_t)
				category="CATEGORY"
				type_product="TYPE_PRODUCT"
				name=rawproduct.iloc[c, 3] ;name=str(name);name='"'+name+'"'

				# for v in vendor_list:
				# 	if v.lower() in name.lower():
				# 		vendor = v
					# elif v.lower() not in name.lower():
				vendor = "VENDOR"
				vendor_code=rawproduct.iloc[c, 1];vendor_code=str(vendor_code)
				slug=slugify(name+'-'+vendor_code)
				price=Create_price(rawproduct.iloc[c,5], rates.usd, 0.15)
				provider=prov
				available, stock = "1", "1"
				productfilenotindb.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
				# print(rawproduct.iloc[c, :], '----------\n')
			except IndexError:
				pass
		c+=1

##########

# softcom(raw_product,db_product,product_file_in_db,product_file_not_in_db,itd,prod_r)


########## Обновление полей available CW

def cw(rawproduct,dbproduct, productfileindb, productfilenotindb,id_t, prod_ex):
	rawproduct = rawproduct.dropna(subset=prod_ex) # Если один из этих столбцов имет NaN строка удаляется
	c=0
	while c < len(rawproduct):
		try:
			p = dbproduct.get(vendor_code=str(rawproduct.iloc[c, 0])) # Попытаться получить объект по vender_code 
			# print(p, "in bd")
			id_product=str(p.id)
			category=str(p.category.id)
			type_product=p.type_product
			name=str(p.name);name='"'+name+'"'
			vendor = p.vendor
			vendor_code= p.vendor_code
			slug=p.slug
			price=str(p.price)
			provider=p.provider
			available, stock = "1", "1"
			productfileindb.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
		except Product.DoesNotExist: # Если объеки отсутсвует в БД формируем файл для импорта
			pass
			try:
				r = rawproduct.iloc[c, :]
				id_t+=1
				id_product=str(id_t)
				category="CATEGORY"
				type_product="TYPE_PRODUCT"
				name=rawproduct.iloc[c, 1] ;name=str(name);name='"'+name+'"'
				vendor = "ColorWay"
				vendor_code=rawproduct.iloc[c, 0];vendor_code=str(vendor_code)
				slug=slugify(name+'-'+vendor_code)
				price=str(rawproduct.iloc[c, 3]); price=price.replace(',','.'); price=round(Decimal(price)*rates.usd, 2);price=str(price)
				provider=prov
				available, stock = "1", "1"
				productfilenotindb.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
				# print(rawproduct.iloc[c, :], '----------\n')
			except IndexError:
				pass
		c+=1

##########

# cw(raw_product,db_product,product_file_in_db,product_file_not_in_db,itd,prod_r)

########## Обновление полей available baden

# def baden(rawproduct,dbproduct, productfileindb, productfilenotindb,id_t):
# 	rawproduct = rawproduct.dropna(subset=b_r) # Если один из этих столбцов имет NaN строка удаляется
# 	c=0
# 	while c < len(list_keys):
# 		try:
# 			p = db_product.get(vendor_code=str(row_dict.get(b_r[0]).get(list_keys[c])).split('.')[0]) # Попытаться получить объект по vender_code 
# 			# print(str(row_dict.get(b_r[0]).get(list_keys[c])).split('.')[0], "in bd")
# 			if str(row_dict.get(b_r[1]).get(list_keys[c])).split('.')[0] == "Есть":
# 				# pass
# 				print("Yes")
# 				# p.available = True; p.save() # Присвоить значение True если в прайсе "В наявності"
# 		except Product.DoesNotExist: # Если объеки отсутсвует в БД формируем файл для импорта
# 			try:
# 				# Если один из этих столбцов имет NaN строка удаляется
# 				r = raw_product.dropna(subset=["Код товара"]).iloc[c, :]
# 				# print(row_dict.get(b_r[0]).get(list_keys[c]), "Not in bd", c)
# 				itd+=1
# 				id_product=str(itd)
# 				vendor="VENDOR"
# 				category="CATEGORY"
# 				type_product="TYPE_PRODUCT"
# 				name=r[1];name=str(name);name='"'+name+'"'
# 				vendor_code=r[0];vendor_code=str(vendor_code)
# 				slug=slugify(name+'-'+vendor_code)
# 				price=r[3];price=str(price);price=price.replace(",",".")
# 				provider=prov
# 				available, stock = "1", "1"
# 				product_file.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
# 				print(r, '----------\n')
# 			except IndexError:
# 				pass
# 		c+=1

##########


########## Обновление полей available ecko

# type_product_list = [('Фильтры', '128'),
# ('Мастер-пленки', '99'),
# ('Зажимы', 'BED_TYPE'),
# ('Лезвие очистки', '128'),
# ('Комплекты обслуживания', '128'),
# ('Коротроны', '128'),
# ('Крепления', '128'),
# ('Экраны', 'BED_TYPE'),
# ('Беспилотные аппараты', 'BED_TYPE'),
# ('Средства ухода', '130'),
# ('Доп.оборудование', 'BED_TYPE'),
# ('Тонер в мешках', '129'),
# ('Игры', 'BED_TYPE'),
# ('Переплетчики', 'BED_TYPE'),
# ('Тонеры', '129'),
# ('Скобы', 'BED_TYPE'),
# ('Уничтожители', 'BED_TYPE'),
# ('Вал заряда', '128'),
# ('Драм-картридж', '129'),
# ('Указки', 'BED_TYPE'),
# ('Термообложки', 'BED_TYPE'),
# ('Втулки', '128'),
# ('Носители', 'BED_TYPE'),
# ('Лезвие дозирующее', '128'),
# ('Шестерни вала тефлонового', '128'),
# ('Аксессуары', 'BED_TYPE'),
# ('Зарядные устройства', 'BED_TYPE'),
# ('Резаки', 'BED_TYPE'),
# ('Пружины', '128'),
# ('Термопленки', '128'),
# ('Бумага', 'BED_TYPE'),
# ('Тормозные площадки', '128'),
# ('Обложки', 'BED_TYPE'),
# ('Сетевое оборудование', 'BED_TYPE'),
# ('Валы', '128'),
# ('Датчики', '128'),
# ('Нагревательные элементы', '128'),
# ('Лезвие очистки ремня', '128'),
# ('Инструмент', 'BED_TYPE'),
# ('Шестерни редуктора', '128'),
# ('Тонер-картридж', '129'),
# ('Сепараторы', '128'),
# ('Офисная техника', 'BED_TYPE'),
# ('Платы', '128'),
# ('Игрушки', 'BED_TYPE'),
# ('Конвертные пленки', 'BED_TYPE'),
# ('Шестерня узла закрепления', '128'),
# ('Шестерни', '128'),
# ('Вал тефлоновый', '128'),
# ('Демонстрационное оборудования', 'BED_TYPE'),
# ('Лампы', '128'),
# ('Лезвие подбора', '128'),
# ('Вал чистящий', '128'),
# ('Другое', 'BED_TYPE'),
# ('Лезвия', '128'),
# ('3D-принтеры', 'BED_TYPE'),
# ('Разное', 'BED_TYPE'),
# ('Ламинаторы', 'BED_TYPE'),
# ('Комплектующие', 'BED_TYPE'),
# ('Металлические пружины', 'BED_TYPE'),
# ('Комплект тонеров', '129'),
# ('Флипчарты', 'BED_TYPE'),
# ('Подшипники', '128'),
# ('Тонер фасованый', '129'),
# ('Узлы закрепления', '128'),
# ('Носимая электроника', 'BED_TYPE'),
# ('Картриджи', '129'),
# ('Пластиковые пружины, спирали', 'BED_TYPE'),
# ('Вал резиновый', '128'),
# ('Вал магнитный', '128'),
# ('Девелоперы', '129'),
# ('Электрооборудование', 'BED_TYPE'),
# ('Блоки изображения', '129'),
# ('Рюкзаки', 'BED_TYPE'),
# ('Лезвие уплотнительное', '128'),
# ('Кульки и коробки упаковочные', '129'),
# ('Термоленты', '128'),
# ('МФУ/Принтеры', 'BED_TYPE'),
# ('Чипы', '129'),
# ('Чернила', '99'),
# ('Фотобарабаны', '129'),
# ('Ролики', '128'),
# ('Конверты', 'BED_TYPE'),
# ('Шлейфы', '128'),
# ('Шестерни вала резинового', '128'),
# ('Ремни', '128')]

# raw_product = pd.read_excel('work_price/ecko.xlsx')
# movies = raw_product[e_r]
# row_dict = movies.dropna(subset=["PartNumber","Название товара","Производитель","Тип","Цена"]).to_dict()

# list_keys = list(row_dict.get(e_r[0]).keys())
# db_product = Product.objects.filter(provider=prov)
# c=0

# product_file=open('sorted_product.csv', 'w')
# product_file.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')
# itd=Product.objects.latest('id').id+1 # Получить последний id + 1

# while c < len(list_keys):
# 	try:
# 		p = db_product.get(vendor_code=row_dict.get(e_r[0]).get(list_keys[c])) # Попытаться получить объект по vender_code
# 		# print(row_dict.get(e_r[0]).get(list_keys[c]), "in bd")
# 		if row_dict.get(e_r[1]).get(list_keys[c]) == "Да":
# 			pass
# 			# print("Yes")
# 			# p.available = True; p.save() # Присвоить значение True если в прайсе "В наявності"
# 		elif row_dict.get(e_r[1]).get(list_keys[c]) == "Нет":
# 			pass
# 			# print("No")
# 			# p.available = False; p.save() # Присвоить значение False если в прайсе "Під замовлення"
# 	except Product.DoesNotExist: # Если объеки отсутсвует в БД формируем файл для импорта
# 		try:
# 			# print(row_dict.get(e_r[0]).get(list_keys[c]), "Not in bd", c)
# 			# Если один из этих столбцов имет NaN строка удаляется
# 			r = raw_product.dropna(subset=["PartNumber","Название товара","Производитель","Тип","Цена"]).iloc[c, :]
# 			itd+=1
# 			id_product=str(itd)
# 			vendor=r[2]; vendor=str(vendor)
# 			for t in type_product_list:
# 				if t[0] == str(r[3]):
# 					type_product ,category = t
# 			name=r[1];name=str(name);name='"'+name+'"'
# 			vendor_code=r[0];vendor_code=str(vendor_code)
# 			slug=slugify(name+'-'+vendor_code)
# 			price = Create_price(price, rates.usd, 0.30)
# 			provider=prov
# 			if str(r[9]) == "Да":
# 				available, stock = "1", "1"
# 			elif str(r[9]) == "Нет":
# 				available, stock = "0", "0"
# 			product_file.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
# 			print(r, '----------\n')
# 		except IndexError:
# 			pass
# 	c+=1

##########

########## Обновление полей available megatrade

# raw_product = pd.read_excel('work_price/megatrade.xlsx')
# movies = raw_product[m_r]
# # Если один из этих столбцов имет NaN строка удаляется
# row_dict = movies.dropna(subset=['Артикул ',
# 								'Номенклатура',
# 								'Стандартна роздрібна ціна',
# 								'Стандартна партнерська ціна']).to_dict()

# list_keys = list(row_dict.get(m_r[0]).keys()) # формирует словарь из DataFrame
# db_product = Product.objects.filter(provider=prov) # Получить queryset
# c=0

# product_file=open('sorted_product.csv', 'w')
# product_file.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')
# itd=Product.objects.latest('id').id+1 # Получить последний id + 1

# while c < len(list_keys):
# 	try:
# 		p = db_product.get(vendor_code=row_dict.get(m_r[0]).get(list_keys[c])) # Попытаться получить объект по vender_code
# 		# print(row_dict.get(m_r[0]).get(list_keys[c]), "in bd")
# 		if row_dict.get(m_r[1]).get(list_keys[c]) == "В наявності":
# 			pass
# 			# print("Yes")
# 			# p.available = True; p.save() # Присвоить значение True если в прайсе "В наявності"
# 		elif row_dict.get(m_r[1]).get(list_keys[c]) == "Під замовлення":
# 			pass
# 			# print("No")
# 			# p.available = False; p.save() # Присвоить значение False если в прайсе "Під замовлення"
# 	except Product.DoesNotExist: # Если объеки отсутсвует в БД формируем файл для импорта
# 		try:
# 			# print(row_dict.get(m_r[0]).get(list_keys[c]), "Not in bd", c)
# 			# Если один из этих столбцов имет NaN строка удаляется
# 			r = raw_product.dropna(subset=['Артикул ',
# 										'Номенклатура',
# 										'Стандартна роздрібна ціна',
# 										'Стандартна партнерська ціна']).iloc[c, :]
# 			itd+=1
# 			id_product=str(itd)
# 			vendor="Ricoh"
# 			category="CATEGORY"
# 			type_product="TYPE_PRODUCT"
# 			name=r[2];name=str(name);name='"'+name+'"'
# 			vendor_code=r[1];vendor_code=str(vendor_code)
# 			slug=slugify(name+'-'+vendor_code)
# 			price=r[5];price=str(price)
# 			price=round(Decimal(price.replace(",","."))*rates.usd, 2); price=str(price)
# 			provider=prov
# 			available, stock = "1", "1"
# 			product_file.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
# 			# print(r, '----------\n')
# 		except IndexError:
# 			pass
# 	c+=1

##########

########## Добавления изображения ecko Рабочий код

# raw_product = pd.read_excel('ecko.xlsx')
# raw_product.dropna(inplace = True)

# movies = raw_product[["PartNumber", "Адрес изображения"]]
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


########## Обновление Цен Рабочий код

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

########################################################################################################################


# raw_product = pd.read_excel('ecko.xlsx')
# # raw_product.dropna(inplace = True)

# movies = raw_product[["PartNumber", "Наличие"]]
# row_dict = movies.head(66).to_dict()

# list_keys = list(row_dict.get("PartNumber").keys())
# db_product = Product.objects.filter(provider='ecko')
# c=0

# while c < len(list_keys):
# 	for i in db_product:
# 		if i.vendor_code == row_dict.get("PartNumber").get(list_keys[c]):
# 			if row_dict.get("Наличие").get(list_keys[c]) == "Да":
# 				print("Yes")
# 				# i.available = True
# 			elif row_dict.get("Наличие").get(list_keys[c]) == "Нет":
# 				print("No")
# 				i.available = False
# 			i.save()
# 	c+=1

# df = pd.read_excel('work_price/baden.xlsx')
# # df=df.dropna() # Скріть все с NaN
# # print(df.head(20))
# print(df.iloc[:, 0:4]) # 962 14050.0 Чернила KW-triO для нумераторов, 20 мл, черные  52     86.58

# df = pd.read_excel('work_price/softcom.xls')
# # df=df.dropna() # Скріть все с NaN
# # print(df.head(20))
# print(df.iloc[:, [2,4,5,7]]) # 2354  MR.JQU11.001 Проектор Acer S1386WH (MR.JQU11.001) NaN  NaN



# def t(x_price, y_list, prov):
# 	raw_product = pd.read_excel(x_price)
# 	raw_product.dropna(inplace = True)
# 	movies = raw_product[y_list]
# 	row_dict = movies.head(60).to_dict()
# 	# raw_product = pd.read_excel(x_price)
# 	# raw_product.dropna(inplace = True)
# 	# # movies = raw_product[y_list]
# 	# row_dict = raw_product.to_dict()

# 	print(row_dict)

# 	list_keys = list(row_dict.get(y_list[0]).keys())
# 	db_product = Product.objects.filter(provider=prov)
# 	c=0
# 	if len(y_list) == 2:
# 		while c < len(list_keys):
# 			for i in db_product:
# 				if i.vendor_code == row_dict.get(y_list[0]).get(list_keys[c]):
# 					if row_dict.get(y_list[1]).get(list_keys[c]) == ("Да" or "Есть" or "В наявності"):
# 						# i.available = True
# 						print("ДА", c)
# 					elif row_dict.get(y_list[1]).get(list_keys[c]) == ("Нет" or " " or "Під замовлення"):
# 						print("НЕТ", c)
# 						# i.available = False
# 	 				# i.save()
# 			c+=1
# 	print(prov*20)

# 	# elif len(y_list) == 1:
# 	# 	while c < len(list_keys):
# 	# 		for i in db_product:
# 	# 			if i.vendor_code == row_dict.get(y_list[0]).get(list_keys[c]):
# 	# 				# i.available = True
# 	# 				print("ДА", c)

# 	# 		c+=1
# # t('ecko.xlsx', e_r, prov)

# # t('megatrade.xlsx', m_r, prov)

# # t('1.xlsx', s_r, prov)

# t('2.xlsx', b_r, prov)

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