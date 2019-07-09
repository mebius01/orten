#!/usr/bin/env python3
# -*- coding: utf-8 -*-

raw_product = open('raw_product.csv', 'r')
sorted_product=open('sorted_product.csv', 'w')
db_product=open('db_product.csv', 'r+')
sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')

data_db = db_product.readlines()
data_raw = raw_product.readlines()

counter=1

# for r in data_raw:
# 	print({str(r).split(';')[0][1:-1]:r})
db_list={}
raw_list={}


for d in data_db:
	d=d.split(';')
	db_list[d[5][1:-1]]=d

for r in data_raw:
	if str(r).split(';')[0] != '':
		r=r.split(';')
		raw_list[r[0][1:-1]]=r

print(len(raw_list))
print(len(db_list))

for d in db_list:
	if d not in raw_list:
		print('part number', d, 'not in raw_product') # если нет значение ("stock";"available") выстовить в ноль
		db_list.get(d)[2]=db_list.get(d)[2][1:-1]
		db_list.get(d)[3]=db_list.get(d)[3][1:-1]
		db_list.get(d)[4]=db_list.get(d)[4][1:-1]
		db_list.get(d)[5]=db_list.get(d)[5][1:-1]
		db_list.get(d)[6]=db_list.get(d)[6][1:-1]
		db_list.get(d)[7]=db_list.get(d)[7][1:-1]
		db_list.get(d)[10]=db_list.get(d)[10][1:-2]
	elif d in raw_list:
		if db_list.get(d)[8].split(',')[0] != raw_list.get(d)[3].split(',')[0]:
			db_list.get(d)[2]=db_list.get(d)[2][1:-1]
			db_list.get(d)[3]=db_list.get(d)[3][1:-1]
			db_list.get(d)[4]=db_list.get(d)[4][1:-1]
			db_list.get(d)[5]=db_list.get(d)[5][1:-1]
			db_list.get(d)[6]=db_list.get(d)[6][1:-1]
			db_list.get(d)[7]=db_list.get(d)[7][1:-1]
			db_list.get(d)[10]=db_list.get(d)[10][1:-2]
			db_list.get(d)[8]=raw_list.get(d)[3]
			print(db_list.get(d), db_list.get(d)[8], raw_list.get(d)[3])

for i in db_list.get('24330'):
	print(i, type(i))
# print(db_list)
"""
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