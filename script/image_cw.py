#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wget

from shop.models import Product
# jpg_dir = os.path.join(settings.BASE_DIR, 'media', 'product')
db_product = Product.objects.filter(provider='cw')
paper=db_product.filter(category='81')
for i in paper:
    if i.vendor_code[-4:] == '_OEM':
        url = 'https://colorway.com/img/paper/full/'+str(i.vendor_code[:-4])+'.jpg'
        i.image='product/'+str(i.vendor_code[:-4])+'.jpg'
        i.save()
    else:
        url = 'https://colorway.com/img/paper/full/'+str(i.vendor_code)+'.jpg'
        i.image='product/'+str(i.vendor_code)+'.jpg'
        i.save()
    try:
        wget.download(url)
    except:
        print(url)
