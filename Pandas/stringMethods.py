# -*- coding: utf-8 -*-
import pandas as pd

orders=pd.read_table("orders.tsv")
print(orders.shape)
print(orders.head())
print(orders.columns)
orders.item_name=orders.item_name.str.upper()#item_name kolonundaki verileri büyük harfle yazar
print(orders.item_name)
print(orders.item_name.str.contains('Chicken'.upper()))#item_name in içerisinde Chicken verisi olup olmadığını verir
#choice_description daki köşeli parantezleri kaldırmak için:
orders.choice_description=orders.choice_description.str.replace('[','').str.replace(']','')
print(orders.choice_description)

