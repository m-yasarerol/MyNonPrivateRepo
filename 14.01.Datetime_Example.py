# Soru: 1 ocak 19001 den 31 aralık 2000' e kadar kaç sefer bir ayın ilk günü pazar olur?
from datetime import datetime
from datetime import timedelta

pazar_sayisi = 0
for yil in range(1901,2001):                    
    for ay in range(1,13):
        if datetime(yil,ay,1).weekday() == 6:   # tüm ayların ilk gününe bakıcak ve pazar olanları ekleyecek.
            pazar_sayisi += 1
print(pazar_sayisi)                             #output: 171
