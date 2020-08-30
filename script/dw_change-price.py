#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
.
├── dw_change-price.py
├── csv
│   └── sorted_product_not_in_db_dw.csv
├── json
│   ├── dw.json
│   └── dw-new.json
└── xlsx
	└── dw.xls

Где:
    dw_change-price.py - исполняющий файл
    json/dw.json - файл экспорта. Это файл со старыми ценами слитый с БД (обязателен!!)
    json/dw-new.json - файл импорта. Этот файл формируется в результате работы dw_change-price.py
    xlsx/dw.xls - Файл с ценами поставщика оттуда скрипт берет цены (Обязателен!!)

"""


import sys
import os
from slugify import slugify
import pandas as pd
import json

# -1 Получить последний id в БД, для формирования ИД-полей с новым товаром
id_t = input("Ввести последний ID в базе (Product.objects.latest('id').id): ")
id_t = int(id_t)
print('последний ID в базе', id_t)

#'cw' 'softcom' 'dw' 'megatrade' 'ecko'
prod_r = ["PartNumber", "Рекоменд. цена"]
prov = 'dw'

csv_header = 'id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n'
product_file_in_db = open('csv/sorted_product_in_db_'+prov+'.csv', 'w')
product_file_not_in_db = open('csv/sorted_product_not_in_db_'+prov+'.csv', 'w')
backup = open('csv/backup_'+prov+'.csv', 'w')
product_file_not_in_db.write(csv_header)

raw_product = pd.read_excel('xlsx/'+prov+'.xls')
# 0 Удалить все ненужные строки. Нужные строки определаются prov_r
raw_product = raw_product.dropna(subset=prod_r)
c = 0
data_list = {}
a, b = 0, 0
# Категории в прайсе и id категорий в BD
type_product_list = [('Фильтры', '128'),
                     ('Мастер-пленки', '99'),
                     ('Зажимы', 'BED_TYPE'),
                     ('Лезвие очистки', '128'),
                     ('Комплекты обслуживания', '128'),
                     ('Коротроны', '128'),
                     ('Крепления', '128'),
                     ('Экраны', 'BED_TYPE'),
                     ('Беспилотные аппараты', 'BED_TYPE'),
                     ('Средства ухода', '130'),
                     ('Доп.оборудование', 'BED_TYPE'),
                     ('Тонер в мешках', '129'),
                     ('Игры', 'BED_TYPE'),
                     ('Переплетчики', 'BED_TYPE'),
                     ('Тонеры', '129'),
                     ('Скобы', 'BED_TYPE'),
                     ('Уничтожители', 'BED_TYPE'),
                     ('Вал заряда', '128'),
                     ('Драм-картридж', '129'),
                     ('Указки', 'BED_TYPE'),
                     ('Термообложки', 'BED_TYPE'),
                     ('Втулки', '128'),
                     ('Носители', 'BED_TYPE'),
                     ('Лезвие дозирующее', '128'),
                     ('Шестерни вала тефлонового', '128'),
                     ('Аксессуары', 'BED_TYPE'),
                     ('Зарядные устройства', 'BED_TYPE'),
                     ('Резаки', 'BED_TYPE'),
                     ('Пружины', '128'),
                     ('Термопленки', '128'),
                     ('Бумага', 'BED_TYPE'),
                     ('Тормозные площадки', '128'),
                     ('Обложки', 'BED_TYPE'),
                     ('Сетевое оборудование', 'BED_TYPE'),
                     ('Валы', '128'),
                     ('Датчики', '128'),
                     ('Нагревательные элементы', '128'),
                     ('Лезвие очистки ремня', '128'),
                     ('Инструмент', 'BED_TYPE'),
                     ('Шестерни редуктора', '128'),
                     ('Тонер-картридж', '129'),
                     ('Сепараторы', '128'),
                     ('Офисная техника', 'BED_TYPE'),
                     ('Платы', '128'),
                     ('Игрушки', 'BED_TYPE'),
                     ('Конвертные пленки', 'BED_TYPE'),
                     ('Шестерня узла закрепления', '128'),
                     ('Шестерни', '128'),
                     ('Вал тефлоновый', '128'),
                     ('Демонстрационное оборудования', 'BED_TYPE'),
                     ('Лампы', '128'),
                     ('Лезвие подбора', '128'),
                     ('Вал чистящий', '128'),
                     ('Другое', 'BED_TYPE'),
                     ('Лезвия', '128'),
                     ('3D-принтеры', 'BED_TYPE'),
                     ('Разное', 'BED_TYPE'),
                     ('Ламинаторы', 'BED_TYPE'),
                     ('Комплектующие', 'BED_TYPE'),
                     ('Металлические пружины', 'BED_TYPE'),
                     ('Комплект тонеров', '129'),
                     ('Флипчарты', 'BED_TYPE'),
                     ('Подшипники', '128'),
                     ('Тонер фасованый', '129'),
                     ('Узлы закрепления', '128'),
                     ('Носимая электроника', 'BED_TYPE'),
                     ('Картриджи', '129'),
                     ('Пластиковые пружины, спирали', 'BED_TYPE'),
                     ('Вал резиновый', '128'),
                     ('Вал магнитный', '128'),
                     ('Девелоперы', '129'),
                     ('Электрооборудование', 'BED_TYPE'),
                     ('Блоки изображения', '129'),
                     ('Рюкзаки', 'BED_TYPE'),
                     ('Лезвие уплотнительное', '128'),
                     ('Кульки и коробки упаковочные', '129'),
                     ('Термоленты', '128'),
                     ('МФУ/Принтеры', 'BED_TYPE'),
                     ('Чипы', '129'),
                     ('Чернила', '99'),
                     ('Фотобарабаны', '129'),
                     ('Ролики', '128'),
                     ('Конверты', 'BED_TYPE'),
                     ('Шлейфы', '128'),
                     ('Шестерни вала резинового', '128'),
                     ('Ремни', '128')]

# Курс $
rates = 27

# Функция расчета цены в грн.


def Create_price(pric, rate, procent):
    pric = str(pric)
    pric = pric.replace(",", ".")
    pric = float(pric)*rate
    procent = float(procent)*float(pric)
    return str(round(pric+procent, 2))


# 1 Открыть файл экспорта dw.json для чтения
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
            if str(raw_product.iloc[c, 9]) == "Да":
                vendor_code_key = data_list.pop(str(raw_product.iloc[c, 0]))
                vendor_code_key.update(
                    {'price': Create_price(raw_product.iloc[c, 5], rates, 0.30)})
                vendor_code_key.update({'available': '1'})
                vendor_code_key.update({'stock': '1'})
                a += 1
# 5 Если ключа нет, формируем новый файл для импорта с новыми товарами
        except KeyError:
            try:
                data_list.pop(str(raw_product.iloc[c, 0]).split('.')[0]+'b')
            except KeyError:
                if str(raw_product.iloc[c, 9]) == "Да":
                    id_t += 1
                    id_product = str(id_t)
                    for t in type_product_list:
                        if t[0] == str(raw_product.iloc[c, 3]):
                            category = t[1]
                            type_product = t[0]
                            name = raw_product.iloc[c, 1]
                            name = '"' + \
                                name.replace(',', '').replace('"', '')+'"'
                            vendor = raw_product.iloc[c, 2]
                            vendor_code = raw_product.iloc[c, 0]
                            vendor_code = str(vendor_code)
                            slug = slugify(name+'-'+vendor_code)
                            price = Create_price(
                                raw_product.iloc[c, 5], rates, 0.30)
                            provider = prov
                            available, stock = "1", "1"
                            product_file_not_in_db.writelines(id_product +
                                                              ',' + category +
                                                              ',' + name +
                                                              ',' + slug +
                                                              ',' + provider +
                                                              ',' + vendor_code +
                                                              ',' + vendor +
                                                              ',' + type_product +
                                                              ',' + price +
                                                              ',' + stock +
                                                              ','+available+'\n')
                            b += 1
        c += 1
# 6 Формируем обновленный файл для экспорта dw-new.json
with open('json/'+prov+'-new'+'.json', 'w') as outfile:
    json.dump(data, outfile)
# 7 Сколько в базе объектов сколько в новом файле
print("in db = ", a, " | ", "not in db = ", b)
