#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from slugify import slugify
import pandas as pd
import json

 #'cw' 'softcom' 'baden' 'megatrade' 'ecko'
prod_r=["PartNumber","Название товара","Производитель","Тип","Цена"]; prov='ecko'

csv_header = 'id,category,name,slug,provider,vendor_code,vendor,type_product,price,stock,available'+'\n'
product_file_in_db=open('csv/sorted_product_in_db_'+prov+'.csv', 'w')
product_file_not_in_db=open('csv/sorted_product_not_in_db_'+prov+'.csv', 'w')
backup = open('csv/backup_'+prov+'.csv', 'w')
product_file_not_in_db.write(csv_header)

raw_product = pd.read_excel('xlsx/'+prov+'.xls')
# 0 Удалить все ненужные строки. Нужные строки определаются prov_r
raw_product = raw_product.dropna(subset=prod_r)
c=0
id_t=0
data_list={}
a, b = 0, 0
