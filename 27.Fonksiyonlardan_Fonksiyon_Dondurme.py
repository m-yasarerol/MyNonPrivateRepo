# Fonksiyonlardan fonksiyon döndürmek
# fonksiyonumuz olacak, onun içinde başka bir fonksiyon daha olacak, ama o içerideki fonksiyonu çalıştırmayacağız ama return ile fonksiyon döndüreceğiz
from re import X


def fonk(x):
    return x*x
a = fonk(3)
print(a)            #9
b = fonk
print(b)            #<function fonk at 0x00000051E093F040> : burada b değişkenine bu fonksiyonu atadım. artık bu b benim için fonk fonksiyonudur.
print(b(5))         #25 : yani fonksiyonları da normal stringler gibi değişkenlere atayabiliriz.

# fonksiyonun içine fonksiyon oluşturalım, o fonksiyonu da içeride çalıştırmayalım da geri döndürelim.
def islem_sec(islem):
    def toplama(*args):
        toplam = 0
        for arg in args:
            toplam += arg
        return toplam
    
    def carpma(*args):
        carpim = 1
        for arg in args:
            carpim += arg
        return carpim
    
    def ortalama(*args):
        return sum(args) / len(args)        # girilen verilerin toplamı / girilen verilerin adedi

    if islem == "toplama":  
        return toplama                      # parantezler olursa o fonk. çalıştırıp onun sonucunu geri döndürmeye çalışır. fonksiyonu fonksiyon olarak atamaz
    elif islem == "carpma":
        return carpma
    elif islem == "ortalama":
        return ortalama

top_fonk = islem_sec("toplama")
print(top_fonk)                             #<function islem_sec.<locals>.toplama at 0x000000FD5CE69A60> : artok top_fonksiyonunu toplama fonksiyonuna atadım.
print(top_fonk(2,3,4,5,6))                  #20

carpma_fonk = islem_sec("carpma")
print(carpma_fonk(4,5,6,6,7))               #29

ortalama_fonk = islem_sec("ortalama")
print(ortalama_fonk(4,5,3,4,0))             #3.2
# önceki yaptığımızdan tek farkı: önceden içerideki fonksiyonu çalıştırıyordum, bu yaptığımızda ise içeride fonksiyonları oluşturup, burada geri döndürüp sonradan çalıştırdım.
# yani bu şekilde fonksionlardan geriye fonksiyon döndürebilirsiniz. bir değişkene atayabilirsiniz. 

# bu neden bizim için önemli?
# bir tane fonk. olacak, kişi ismi seçeceğiz, bir fonk. daha olacak, o da takım seçtirecek
def kisi_sec(kisi):
    def takim_sec(takim):
        return f"{kisi}, {takim} takimini tutuyor."
    return takim_sec
a = kisi_sec("Ali")                         # a değişkeni bir takım_sec fonksiyonudur.
b = kisi_sec("Veli")                        # b değişkeni bir takım_sec fonksiyonudur.

print(a("Fenerbahçe"))                      # Ali, Fenerbah�e takimini tutuyor.
print(b("Beşiktaş"))                        # Veli, Be�ikta� takimini tutuyor.
# burada a ve b değişkenleri, oluşturulduğunda içlerinde ilk başta verilen parametreyi de unutmuyorlar.
