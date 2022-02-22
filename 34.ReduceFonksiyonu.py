# Reduce fonksiyonu
# reduce fonk. bir anlamda map ve filter fonksiyonuna benziyor. bir anlamda da farklı
# benzerlikler: reduce fonk. da parametre olarak bir tane fonk. ve bir tane liste alıyor
# farkı: map ve filter fonk. bize liste döndürüyordu. ancak reduce fonk. bize sadece bir tane değer döndürür
# reduce fonk. functools modülünün içinde. önce import etmeliyim
from functools import reduce
from math import gcd    
liste = [2,4,6,9]
def toplama(x,y):
    return x + y
def carpma(x,y):
    return x * y
sonuc1 = reduce(toplama,liste)
print(sonuc1)           #21
# 21 nasıl hesaplandı?
# işlem a : 2 + 4 = 6
# işlem b : 6 + 6 = 12
# işlem c : 12 + 9 = 21
sonuc2 = reduce(carpma,liste)
print(sonuc2)           #432
# 423 nasıl hesaplandı?
# işlem a : 2 * 4 = 8
# işlem b : 8 * 6 = 48
# işlem c : 49 * 9 = 423

# bunu lambda ile de kullanabilirim
sonuc3 = reduce(lambda x,y: x + y,liste)
print(sonuc3)           #21
sonuc4 = reduce(lambda x,y: x * y,liste)
print(sonuc4)           #432

# biraz anlamlı örneklere doğru ilerleyelim
# listenin ekokunu almak istersem ne yapacağım, phytonda ebob var ama ekok yok.
liste = [2,4,6,9,10]    # ebob(a,b)*ekok(a,b) = a*b     ekok(a,b) = a * b / ebob(a,b)
def ekok(a,b):          # bu fonk bize iki sayının ekokunu döndürecek
    return int((a * b) / gcd(a,b))
print(ekok(6,8))        #24

ekok_ = reduce(ekok,liste)
print(ekok_)            #180
# 180 nasıl hesaplandı?
#> ilk önce 2 ile 4 'ün ekoku alındı, 4 oldu
#> 4 ile 6'nın ekoku alındı, 12 oldu
#> 12 ile 9'un ekoku alındı, 36 oldu
#> 36 ile 10'un ekoku alındı,  180 ol

# arka planda neler olduğunu görebilmek için bir örnek yapalım. 
# taş kağıt makas oyunu oyunu oynayan bir programcık yazalım
def tas_makas(b,c):         # burada hangisinin başladığının bir önemi yok. burada kümeden faydalanacağım
    kume = {b,c}
    if b == c:              # ikisi aynı değeri döndürdüyse(taş-taş)
        return b
    if kume == {"taş","makas"}:
        return "taş"
    if kume == {"taş","kağıt"}:
        return "kağıt"
    if kume == {"kağıt","makas"}:
        return "makas"
liste = ["taş","kağıt","taş","makas","kağıt","makas","taş"]
sonuc5 = reduce(tas_makas,liste)
print(sonuc5)               # taş
# arka planda ne oldu?
# önce taş ve kağıt işleme girdi, kağıt kazandı
# kağıt ve taş işleme girdi, kağıt kazandı
# kağıt ile makas işleme girdi, makas kazandı
# makas ile makas işleme girdi, makas kazandı
# makas ile taş işleme girdi, taş kazandı.
