# -*- coding: utf-8 -*-
import pandas as pd

films=pd.read_csv("imdb-1000.csv")
print(films)
print("****1***")

print(films.columns)
print("****2***")
print(films.head())
print(films.tail())
print("****2***")
print(films["title"].head())#il 5 filmin başlığı
print("****3***")
print(films.title)#film isimleri
print("****4***")
print(films[["title","star_rating"]].head())#ilk 5 filmin başlık ve puanlamalarını getirir
print("****5***")
print(films[:9][["title","star_rating"]].head())
print("****6*******")
print(films[films["star_rating"]>8.5])#filmlerden oyu 8.5 ten büyük olanları getirir
print(films[(films["star_rating"]>=8.5)&(films["star_rating"]<=9.0)][["title","star_rating"]])#oyu 8.5 VE 9.0 arasında olan  filmlerin adını ve oylarını getirir
print(films[(films["star_rating"]>=9.5)|(films["star_rating"]<=7.4)][["title","star_rating"]])#oyu 9.5 tan büyük VEYA 7.4 ten küçük olan  filmlerin adını ve oylarını getirir

