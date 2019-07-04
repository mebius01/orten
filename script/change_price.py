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

for d in data_db:
	d=d.split(';')
	print(str({d[5][1:-1]:d}.keys()))
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