#!/usr/bin/env python3
# -*- coding: utf-8 -*-

corrective_value = input("Корректирующие значение : "); corrective_value=float(corrective_value)
raw_product = open('raw_product.csv', 'r')
sorted_product=open('sorted_product.csv', 'w')

sorted_product.write('id,category,name,slug,provider,vendor_code,vendor,specifications,type_product,price,stock,available'+'\n')
data = raw_product.readlines()

for i in data:
	i=str(i).split(';')
	print(i)
	a=i[9]; a=float(a[1:-1])
	b=a/corrective_value; b=format(b, '.2f');
	i[9]=str(b)
	print(i[5], a, b)
	sorted_product.writelines(i[0]+','+i[1]+','+i[2]+','+i[3]+','+i[4]+','+i[5]+','+i[6]+','+i[7]+','+i[8]+','+i[9]+','+i[10]+','+i[11])

raw_product.close()
sorted_product.close()