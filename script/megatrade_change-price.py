#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from slugify import slugify
import pandas as pd
import json
from decimal import Decimal

rates = 24.2

#'cw' 'softcom' 'baden' 'megatrade' 'ecko'
prod_r = ['Артикул ', 'Номенклатура',
          'Стандартна роздрібна ціна', 'Стандартна партнерська ціна']
prov = 'megatrade'  # megatrade

csv_header = 'id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n'
product_file_in_db = open('csv/sorted_product_in_db_'+prov+'.csv', 'w')
product_file_not_in_db = open('csv/sorted_product_not_in_db_'+prov+'.csv', 'w')
backup = open('csv/backup_'+prov+'.csv', 'w')
product_file_not_in_db.write(csv_header)

raw_product = pd.read_excel('xlsx/'+prov+'.xls')
# 0 Удалить все ненужные строки. Нужные строки определаются prov_r
raw_product = raw_product.dropna(subset=prod_r)
c = 0
id_t = 14918
data_list = {}
a, b = 0, 0
# 1 Открыть файл экспорта baden.json для чтения
with open('json/'+prov+'.json') as json_file:
    data = json.load(json_file)
# 2 Поля available и stock обнулить'
    for i in data:
        i.update({'available': '0'})
        i.update({'stock': '0'})
    print('all products = available 0 stock 0')
# 3 Формируем данные вида 235435: {'id': 4005, 'category': 62, 'name': 'Кольцо ...} 235435 <-vendor_code
    for i in data:
        data_list[i.get('vendor_code')] = i
# 4 В цикле пытаемся получить словарь по ключу '235435'
# Если ключ есть обновляем существующие данные
    while c < len(raw_product):
        try:
            if str(raw_product.iloc[c, 2]) == "В наявності":
                vendor_code_key = data_list.pop(str(raw_product.iloc[c, 0]))
                vendor_code_key.update({'price': Decimal(round(float(str(raw_product.iloc[c, 4]).replace(",", "."))*rates, 2))})
                vendor_code_key.update({'available': '1'})
                vendor_code_key.update({'stock': '1'})
                a+=1
# 5 Если ключа нет, формируем новый файл для импорта с новыми товарами
        except KeyError:
            if str(raw_product.iloc[c, 2]) == "В наявності":
                id_t += 1
                id_product = str(id_t)
                vendor = "Ricoh"
                category = "CATEGORY"
                type_product = "TYPE_PRODUCT"
                name = str(raw_product.iloc[c, 1])
                name = '"'+name.replace(',', '').replace('"', '')+'"'
                vendor_code = str(raw_product.iloc[c, 0])
                slug = slugify(name+'-'+vendor_code)
                price = str(raw_product.iloc[c, 4])
                price = round(float(price.replace(",", "."))*rates, 2)
                price = str(price)
                provider = prov
                available, stock = "1", "1"
                product_file_not_in_db.writelines(id_product+','+category+','+name+','+slug+','+provider +
                                                    ','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
                b+=1
        c+=1
# 6 Формируем обновленный файл для экспорта baden-new.json
with open('json/'+prov+'-new'+'.json', 'w') as outfile:
    json.dump(data, outfile)
# 7 Сколько в базе объектов сколько в новом файле
print("in db = ", a, " | ", "not in db = ", b)


# # Обновление полей available megatrade
# def megatrade(rawproduct, dbproduct, productfileindb, productfilenotindb, id_t, prod_ex):
#     rates = Rates.objects.latest('created')
#     # Если один из этих столбцов имет NaN строка удаляется
#     rawproduct = rawproduct.dropna(subset=prod_ex)
#     c = 0
#     while c < len(rawproduct):
#         try:
#             # Попытаться получить объект по vender_code
#             p = dbproduct.get(vendor_code=str(rawproduct.iloc[c, 0]))
#             if str(rawproduct.iloc[c, 2]) == "В наявності":
#                 id_product = str(p.id)
#                 category = str(p.category.id)
#                 type_product = p.type_product
#                 name = str(p.name)
#                 name = '"'+name.replace(',', '').replace('"', '')+'"'
#                 vendor = '"'+p.vendor+'"'
#                 vendor_code = '"'+p.vendor_code+'"'
#                 slug = p.slug
#                 price = round(
#                     Decimal(str(rawproduct.iloc[c, 4]).replace(",", "."))*rates.usd, 2)
#                 price = str(price)
#                 provider = p.provider
#                 available, stock = "1", "1"
#                 productfileindb.writelines(id_product+','+category+','+name+','+slug+','+provider +
#                                            ','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
#                 # Попытаться получить объект по vender_code
#                 print(p, vendor_code, price)
#         # elif row_dict.get(m_r[1]).get(list_keys[c]) == "Під замовлення":
#         # 	pass
#             # print("No")
#             # p.available = False; p.save() # Присвоить значение False если в прайсе "Під замовлення"
#         except Product.DoesNotExist:  # Если объеки отсутсвует в БД формируем файл для импорта
#             try:
#                 if str(rawproduct.iloc[c, 2]) == "В наявності":
#                     id_t += 1
#                     id_product = str(id_t)
#                     vendor = "Ricoh"
#                     category = "CATEGORY"
#                     type_product = "TYPE_PRODUCT"
#                     name = str(rawproduct.iloc[c, 1])
#                     name = '"'+name.replace(',', '').replace('"', '')+'"'
#                     vendor_code = str(rawproduct.iloc[c, 0])
#                     slug = slugify(name+'-'+vendor_code)
#                     price = str(rawproduct.iloc[c, 4])
#                     price = round(
#                         Decimal(price.replace(",", "."))*rates.usd, 2)
#                     price = str(price)
#                     provider = prov
#                     available, stock = "1", "1"
#                     productfilenotindb.writelines(id_product+','+category+','+name+','+slug+','+provider +
#                                                   ','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
#                     print(rawproduct.iloc[c, :])
#             except IndexError:
#                 pass
#         c += 1
# ##########
