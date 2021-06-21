# -*- coding: utf-8 -*-
import pandas as pd

notlar=pd.read_csv("grades+(1).csv")
print(notlar)
print("************1************")
print(type(notlar))#DataFrame
print("*************2************")
print(notlar.head())
print("************3*************")
print(notlar.tail())
print("**********4************")
print(notlar["Last name"])#Last name kolonunu getirir
print("**************5*********")
#print(notlar["First name"])#hata verir çünkü First name de tırnka("") var. Bunu düzeltelim:
notlar.columns=["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar["Final"])
print("*********6***********")
print(notlar.iloc[2])#2 numaralı indeksteki verinin bilgilerine ulaştık
print("**********7*******")
print(notlar[0:10])#0 dan 10 a kadar olan verileri getirir 




















