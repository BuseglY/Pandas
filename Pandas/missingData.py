# -*- coding: utf-8 -*-
import pandas as pd

url="http://bit.ly/uforeports"

data=pd.read_csv(url)
print(data[["City","Colors Reported","Shape Reported","State","Time"]].head())
print(data.columns)
print(data.isnull().head())#il 5 data için null mı değerini verir
#NaN->not a number(olmayan data)
print(data.notnull().head())#ilk 5 data için boş değil mi değerini verir
print(data.isnull().sum())#boş olanların toplamını verir(her kolon için)
print(data[data.City.isnull()])#City bilgisi boş olan verileri getirir
 
#DROPNA(Silmek-Uçurmak)->uyumsuz verileri uçurabilmek için
print(data.shape)#kaç tane datamız var?(18241 data,5 kolon)
#data=data.dropna()#herhangi bir kolonda boş data varsa o dataları siler(NaN olanları)
#print(data.shape)#(2486,5)
#data=data.dropna(how="any")#herhangi bir kolonda boş data varsa o datayı satır olarak siler.Yukarıdaki ile aynıdır
#print(data)
#data=data.dropna(how="all")#bütün kolonların NaN olduğu veriyi satır olarak siler
#print(data.shape)#(18241 rows x 5 columns)->bütün kolonları NaN olan veri yokmuş.
#data=data.dropna(subset=['City','Colors Reported'],how="all")#bir data da hem City hem de Colors Reported bilgisi yoksa o veriyi siler
#print(data.shape)#(18221, 5)
#data=data.dropna(subset=['City','Colors Reported'],how="any")#bir datanın City ya da Colors Reported bilgilerinden bir tanesi bile NaN ise o veriyi siler
#print(data.shape)#(2877, 5)

#FILLNA(Doldurmak)->verilerimizi belirli bir değer ile doldurabilmemizi sağlar.
print(data['Shape Reported'].fillna(value='Belirsiz',inplace=True))#Shape Reported kolonunda 'NaN' olan verileri 'Belirsiz' olarak değiştirir ve inplace(bellekteki yer)ini değiştirir
print(data['Shape Reported'].value_counts(dropna=False))#Shape Reported kolonunun aldığı değerlerin sayısını getirir.Dropna işlemi yaptırmamak için False dedik

print(data.shape)










































