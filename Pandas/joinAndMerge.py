# -*- coding: utf-8 -*-
import pandas as pd

data1={
       'id':[1,2,3,4],
       'ad':['Engin','Derin','Salih','Buse'],
       'soyad':['Demiroğ','Demiroğ','Demiroğ','Yılmaz']
       }

data2={
       'id':[1,3,4,7],
       'ad':['Ayşe','Ali','Ahmet','Cemal'],
       'soyad':['Demiroğ','Demiroğ','Demiroğ','Yılmaz']
       }

data1Df=pd.DataFrame(data1)
data2Df=pd.DataFrame(data2)

print(data1Df)
print(data2Df)

#JOIN

print(pd.merge(data1Df,data2Df,on='id',how='inner'))#id alanına göre join işlemi yapar.Join türünü belirttik
print("*****************")
print(pd.merge(data1Df,data2Df,on='id',how="left"))#id ye göre sol tarafta olup sağda olmayanlara NaN değeri vererek getirir
print(pd.merge(data1Df,data2Df,on='id',how="right"))#id ye göre sağ tarafta olup solda olmayanlara NaN değeri vererek getirir


#CONCAT(birleştirmek)
print(pd.concat([data1Df,data2Df]))#aşağıya doğru ekler
print(pd.concat([data1Df,data2Df],axis=1))#sağa doğru ekler.axis=0->aşağıya doğru ekler


















