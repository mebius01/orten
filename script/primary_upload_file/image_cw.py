#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wget

from shop.models import Product
jpg_dir = 'media/product'

ink = 'https://colorway.com/img/ink/full/'
paper = 'https://colorway.com/img/paper/full/'
tonercartridge = 'https://colorway.com/img/tonercartridge/full/'
toner = 'https://colorway.com/img/toner/full/'
inkcartridge = 'https://colorway.com/img/inkcartridge/full/'
cleaner = 'https://colorway.com/img/cleaner/full/'

db_product = Product.objects.filter(provider='cw')

cat_ink = db_product.filter(category='82')
cat_paper = db_product.filter(category='81')
cat_tonercartridge = db_product.filter(category='84')
cat_toner = db_product.filter(category='83')
cat_inkcartridg = db_product.filter(category='85')
cat_cleaner = db_product.filter(category='168')

cat_all = [cat_ink, cat_paper, cat_tonercartridge, cat_toner, cat_inkcartridg, cat_cleaner]

for i in cat_tonercartridge:
    if i.vendor_code[-4:] == '_OEM':
        url = tonercartridge +str(i.vendor_code[:-4])+'.jpg'
        try:
            wget.download(url, jpg_dir)
            i.image='product/'+str(i.vendor_code[:-4])+'.jpg'
            i.save()
        except:
            print(url)
    else:
        url = tonercartridge + str(i.vendor_code)+'.jpg'
        try:
            wget.download(url, jpg_dir)
            i.image='product/'+str(i.vendor_code)+'.jpg'
            i.save()
        except:
            print(url)

