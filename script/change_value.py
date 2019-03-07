#!/usr/bin/env python3
# -*- coding: utf-8 -*-

raw_product = open('raw_product.csv', 'r')
sorted_product=open('sorted_product.csv', 'w')
db_product=open('db_product.csv', 'r+')
sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')

data_raw = list(set(raw_product.readlines()))
data_db
for i in data_raw:
	i=str(i).split(';')
	vendor_code=i[0]
	for ii in data_db:
		if ii[5][1:-1] == str(vendor_code):
			if i[7] == '"Y"':
				available, stock = "1", "1"
			elif i[7] == '"N"':
				available, stock = "0", "0"
			print(vendor_code, available, stock)






raw_product.close()
sorted_product.close()