import pandas as pd
import numpy as np

data=np.array(["Engin","Derin","Salih"])
s=pd.Series(data,index=[1,2,3])#datanın pandas ta serisini oluşturduk
print(s)
print(s[1])#Engin değerini verir.s[0] da key hatası verir.çünkü bizim indekslerimiz 1 den başlıyor

data2={"matematik":10,"fizik":20,"beden eğitimi":100}
s2=pd.Series(data2,index=["fizik","matematik","beden eğitimi"])#önce fiziği yazar çünkü indekste ilk sıraya fiziği koyduk
print(s2)

print(s2[0])#fiziğin değerini verir çünkü 0.indekste fizik var.
print(s2["matematik"])#10

s3=pd.Series(5,index=[1,2])#indekslerin hepsinde 5 değerini verir.
print(s3)

