# -*- coding: utf-8 -*-
import pandas as pd

notlar=pd.read_csv("grades+(1).csv")
notlar.columns=["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar)
print("*********1***********")
#Indexing
print(notlar.loc[:,"İsim"])#bütün satıların isim kolonunu getirir
print("*********2************")
print(notlar.loc[:5,"İsim"])#0 dan 5 e kadarki(pandas ta 5 dahil) verileri getirir
print("**********3**********")
print(notlar.loc[:5,"İsim":"Test4"])#5.indeksteki satıra kadar(5 dahil) İsim kolonundan Test4 kolonuna kadar(Test4 dahil)olan veri bilgilerini getirir
print("*****4*******")
print(notlar.loc[:5,["İsim","Soyisim","Final"]])#5.indekse kadarki verilerin İsim VE Final kolonlarını getirir
print("******5*******")
print(notlar.loc[:5,:"Test2"])#5.indekse kadarki verilerin Test2 kolonuna kadarki bilgilerini getirir
print("******6*******")
print(notlar.loc[::-1,"İsim"])#::-1 tersten sıralar.Verileri aşağıdan başlayarak isim kolonu bilgisi dahilinde getirir

