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


# https://colorway.com/img/ink/full/CW-LHW130LM01.jpg
# https://colorway.com/img/paper/full/PG26061030RL.jpg
# https://colorway.com/img/tonercartridge/full/CW-DR-H232M.jpg
# https://colorway.com/img/toner/full/TH-4200P.jpg
# https://colorway.com/img/inkcartridge/full/CW-H141XL-I.jpg
# https://colorway.com/img/cleaner/full/CW-5230.jpg