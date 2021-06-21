# -*- coding: utf-8 -*-
import pandas as pd

data=[10,20,30,40,50]
df=pd.DataFrame(data)#DataFrame de indeksler ve kolonlar vardır
print(df)

data2=[["Engin",33,"Ankara"],["Derin",4,"Ankara"],["Salih",32,"İstanbul"]]
df2=pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index=[1,2,3])#kolon isimleri ve indeks değerlerini verdik
print(df2)
print("**********1**********")

data3={"İsim":["Engin","Derin","Salih"],
       "Yaş":[33,4,32],
       "Şehir":["Ankara","Ankara","İstanbul"]}
df3=pd.DataFrame(data3,index=[1,2,3],columns=["İsim","Yaş","Şehir"])
print(df3["İsim"])#Sadece isim kolonunu getirir
print(df3["Yaş"])

#del df3["Şehir"]#Şehir kolonunu sildik
#df3.pop("Şehir")#Şehir kolonunu sildik
print(df3)

print("***********2***************")
print(df3.loc[2])#Derin.isimlendirdiğimiz indeks değerine göre datayı getirir
print(df3.iloc[1])#Derin. 0 dan başlayıp 1.indeksteki değeri verir.

df4=df3.append(df2)#append->dataları birleştirir
print(df4)
print("************3*************")
print(df4.head())#ilk 5 veriyi getirir
print("****************4**************")
print(df4.tail())#son 5 veriyi getirir
















