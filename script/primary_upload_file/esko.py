#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from slugify import slugify
import pickle

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


int_counter = open('counter_id.pkl', 'rb')
counter = pickle.load(int_counter)
int_counter.close()
counter=input("последнее id Продукта в BD: ") or counter; counter=int(counter)

provider = "ecko"

print(counter)

price_file = open('raw_product.csv', 'r')
product_file=open('sorted_product.csv', 'w')
product_file_long=open('long_sorted_product.csv', 'w')
data = price_file.readlines()
product_file.write('id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n')

for i in data:
	i=str(i).split(';')
	id_product=str(counter)
	vendor_code=i[0]
	name=i[1]
	vendor=i[2]
	slug=slugify(name+'-'+vendor_code)
	print(vendor_code, i[5])
	price=str(i[5]); price=((float(price.replace(",","."))*0.30)+float(price.replace(",",".")))*28; 
	price=format(price, '.2f')
	price=str(price)
	if i[9] == '"Нет"':
		available, stock = "0", "0"
	elif i[9] == '"Да"':
		available, stock = "1", "1"
	for t in type_product_list:
		if t[0] == i[3][1:-1]:
			type_product ,category = t
	product_file.writelines(id_product+','+category+','+name+','+slug+','+provider+','+vendor_code+','+vendor+','+type_product+','+price+','+stock+','+available+'\n')
	counter+=1

print(counter)

out_counter = open('counter_id.pkl', 'wb')
pickle.dump(counter, out_counter)
out_counter.close()

"""
prod=Product.objects.get(vendor_code='DRS55-A')
>>> prod
<Product: Мастер-пленка AEBO Duplo A3 DP 550S/ J 450/ 306 x 113 m/ DRS55>
>>> prod.image
<ImageFieldFile: None>
>>> prod.image = 'product/77356.JPG'
>>> prod.save()
"""