#input fonksiyonu
# ÖRNEK1: ekrandan alınan bir sayının faktoriyelini hesaplayan bir program yazınız.
sayi = int(input("Bir sayı giriniz: ")) #bu şekilde girilen ifadeyi integer çevirdim.
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
# inpput : 5
# output: 5! = 120

#while döngüsü ile yapalım
sayi = int(input("Bir sayı giriniz: "))
faktoriyel = 1
i = 2
while i <= sayi:
    faktoriyel *=  i
    i += 1
print(f"{sayi}! = {faktoriyel}")
#aynı sonucu verdi.
# ama kullanıcı string bir ifade girerse program hata verir. ilerde onun için de ayrı bir değer döndüreceğiz

# Örnek 2: ekrandan alınan bir sayının asal olup olmadığını kontrol eden bir program yazınız.
sayi = int(input("Bir sayı giriniz: ")) #sayısı aldım
prime = True                            #sayıyı asal kabul ettim
#tüm sayılar 1'e bölüneceği için phyton tüm sayıları asal algılar. o nedenle 1 yazdım.
for i in range(2,sayi):                 #sayılardan herhangi birisine bölünür ise..
    if sayi %i == 0:
        prime = False                   #prime değişkeni false olur
        break
if prime == True:
    print(f"{sayi} sayısı asaldır.")     
else:
    print(f"{sayi} sayisi asal değildir.")

# Örnek 3 : ekrandan alınan sayının pozitif kaç tane böleni olduğunu bulan bir program yazınız.
sayi = int(input("Bir sayi giriniz:"))
bolen_sayisi = 0
for i in range(1, sayi +1):
    if sayi %i == 0:
        bolen_sayisi += 1               #sayi bölündükçe bölen sayisini 1 arttirir.
print(f"{sayi} sayisinin {bolen_sayisi} tane böleni vardır.")

# ekrandan okunan bir sayının rakamlarını toplayan bir program yazınız.
sayi = int(input("Bir sayi giriniz: "))
str_sayi = str(sayi)                    # stringlerde for döngüsü kullanılabildiği için bu sayıyı stringe çevirdim.
toplam = 0
for rakam in str_sayi:
    toplam += int(rakam)                #toplayabilmek için sayıyı rakama çevirdim.
print(toplam)
# bir de stringe çevirmeden çözelim
sayi = int(input("Bir sayı giriniz: "))
toplam = 0
gecici_sayi = sayi
while gecici_sayi != 0:
    basamak = gecici_sayi % 10
    toplam += basamak                   #10 a bölümünden kalanı toplama ekledi
    gecici_sayi //= 10                  #ona bölümünden kalanı çıkarıp döngüye devam etti "// tam bölünenleri alır."
print(toplam)
#  YUKARIDAKİ ÇÖZÜM ŞEKLİNİ ANLAMADIM.

#ekrandan peşpeşe okunan sayının 5 sayının en büyüğünü ekrana yazdıran bir program yazınız.
liste = []
for i in range(5):
    sayi = int(input("Bir sayı giriniz: "))
    liste.append(sayi)                  #kullanıcıdan 5 kez sayı alır ve listeye ekler.
print(f"En büyük sayi : {max(liste)}")
print(f"En büyük sayi : {min(liste)}")
# burada da bir döngü yardımı ile 5 kez sayı istedik, hepsini listeye ekledik ve en küççük ve en büyük elemanlarını yazdırdık.

# Ekrandan okunan bir sayının herhagi bir sayının karesi olup olmadığını kontrol eden bir program yazınız.
sayi = int(input("Bir sayi giriniz: "))
karekok = sayi ** 0.5
if karekok == int(karekok):
    print("Tamkare")
else:
    print("Tamkare değil")
#burada ne yaptık: bir sayının karekökünü tanımladım (karekok = sayi ** 0.5) eğer tam sayı çıkarsa birbirine eşitleniyor. (int(karekok)) tam sayıya çeviriyor.
# bu şekilde bir sayının tamkare olup olmadığını kontrol ettik.

#Ekrandan okunan bir metinde hangi harfin kaç kez kullanıldğını gösteren bir program yazınız.
metin = input("Bir metin giriniz: ")
sozluk = dict()                     #sözlüğüm ilk başta boş
for harf in metin:
    if harf in sozluk:
        sozluk[harf] += 1           # harf ,sözlükte zaten var ise adet bilgisine 1 ekle.
    else:
        sozluk[harf] = 1            #sözlükte olmayan bir değeri 1 yap
for harf,adet in sozluk.items():
    print(harf,adet)

# ekrandan okunan bir metinde a harflerini büyük yapan bir program yapalım.
metin = input("bir metin giriniz: ")
metin2 = ""
for harf in metin:                  # kodun algoritması
    if harf == "a":                 # a harfiyle karşılaşırsan
        metin2 += "A"               # metne büyük a (A) ekle
    else:                           # a harfi dışında bir harf geldiğinde.
        metin2 += harf              # değişiklik yapmadan ekle.
print(metin2)                       # ve sonucu yazdır.
