# # # Fonksiyon kavramı ve önemi
# # # Fonksiyonları tanımlama ve çalıştırma
# # parametre almayan ve ve alan fonksiyonlar
# # return anahtar kelimesi
# # parametlerele varsayılan değerler atamak

# # diyelim ki bir web sitemiz var. kullanıcılarımız burada çeşitli işlemler gerçekleştiriyor. başarıyla gerçekleşen her işlem için bir değer döndürüyoruz.
# 1- kullanıcı giriş yaptı : print("şlkem başarılı")
# 2- kullanıcı fotoğraf ekledi : print("şlkem başarılı")
# 3- kullanıcı fotoğraf sildi : print("şlkem başarılı")
# 4- kullanıcı yorum yaptı : print("şlkem başarılı")
# 5- kullanıcı beğeni attı : print("şlkem başarılı")
# 6- kullanıcı yorum paylaştı : print("şlkem başarılı")
# 7- kullanıcı çıkış yaptı : print("şlkem başarılı")
# burada 7 kez işlem başarılı dedik. bu büyük projelerde çok daha fazla sayıda olabilir. programda aynı kodu 20 farklı yerde kullanabiliriz. ama her kullandığımız yerde ayrı ayrı yazarsak hem kod uzar, hem de esnek bir yazılım olmaz. monoblok bir yazılım olmaz. kodda bir değişiklik yapmak istersen sıkıntı yaşarsın.
# # fonk. bize burada yardımzı oluyor. Fonksiyonlar tekrar tekrar kullanacağımız bir kod varsa, onu fonk. olarak tanımlayıp, gerektiğinde tekrar kullanmamızı sağlar.
# ör:
def bilgi_ver():
    print("İşlem başarılı")
bilgi_ver()
bilgi_ver()
bilgi_ver()
bilgi_ver()
bilgi_ver()
bilgi_ver()
# günün birinde bilgi mesajnı değiştirmek istersen tek fonksiyonu değiştirmen yeterli olacak. yani tekrar tekrar kullanacağın bir kod parçasını fonk . olarak tanımlarsan onu değiştirmek daha kolay, kodun daha sade olur.
# aynı şeyi tekrar tekrar yazmamızın önüne geçiyor
# def fonksiiyon tanımlayacağımızı belirkeyen anahtar kelime, deften sonra gelen isim fonksiyonun ismi
# altındaki blok fonksiyonun kod bloğudur. fonksiyon çağrıldığında bloğun içerisi çalışır.
# fonksiyonun ismini yazıp parantez açıp kapatırsan fonksiyonu çağırmış olursun. parantezi unutma.
# ör2
def selamla():
    print("Merhaba")
selamla()

# gelelim parantezlerin içerisine, parantezin içi boş olduğunda fonk. her çağırdığında aynı işlemi yapar. ancak bazen fonk. bazı parametreler girmem gerekebilir.
# ÖR:
def selamla(isim):
    print("Merhaba " + isim)
selamla("Ahmet")

# bir de iki adet parametre alan bir fonk. görelim.
def topla(x,y):
    print(f"x + y = {x + y}")
topla(3,6)
#ör:
def carp(x,y):
    print(f"x * y = {x * y}")
carp(3,6)
# yani fonksiyonumun beklediği parametreye uygun olarak çağırmam gerekir. tanımladığım parametre sayısı ile, çağırırken kullandığım parametre sayısı uyumlu olmalıdır.
#içine liste alan bir fonksiyon yazalım
def ortalama_hesapla(liste):
    toplam = sum(liste)
    adet = len(liste)               #listenin uzunluğu, hatırla.
    ortalama = toplam / adet
    print(f"Girilen sayılarn ortalaması: {ortalama}")
#ortalama_hesapla(5)                #eror!: fonksiyonun içinde listelere ait metotlar kullandım ama çağırırken tek bir parametre girdim.
ortalama_hesapla([1,2,3,4,5,6])     #>>Girilen say�larn ortalamas�: 3.5

# başka bir örnek: web sitenin kayt adresinde hepsini büyük harfe çeviren program yazalım
def buyuk_harfe_cevir(metin):
    metin = metin.upper()
    print(metin)
#buyuk_harfe_cevir(123)              #eror!: fonksiyonun içine stringlere ait parametreler girdim ama fonksiyonu çağırırken integer kullandım.
buyuk_harfe_cevir("AnSypRk")        #>>ANSYPRK : inanılmaz değil mi 
# ilerleyen zamanlarda fonksiyonlara fonksiyon olarak parametre vereceğiz.

# başka bir örnek:
def selamla(mesaj, isim):
    print(f"{mesaj} {isim}")
selamla("Merhaba" , "Ahmet")        #>> Merhaba Ahmet

#Ahmeti girmeseydim hata verirdi. ama bazı durumlarda baz parametreler opsiyonel olabilir, yani kullanıcı istediği zaman girer istemediğinde girmez. yani eğer oraya hiçbirşey yazmazsak, bir varsaylan değeri var onu göze alır.
# örneğin aşağıda programa kullanıcı ismini girmezse anonim olsun
def selamla(mesaj, isim = "Anonim"):
    print(f"{mesaj}, {isim}")
selamla("Merhaba")                  #>> Merhaba, Anonim

#başka bir örnek
def indirim_yap(fiyat,yuzde):
    indirim_miktari = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktari
    print(f"İndirimli tutar: {indirimli_fiyat}")
indirim_yap(50,10)                  #>> 45
# yüzde belirtilmezse 20 olsun
def indirim_yap(fiyat,yuzde = 20):
    indirim_miktari = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktari
    print(f"İndirimli tutar: {indirimli_fiyat}")
indirim_yap(50)                  #>> 40
# parametrelere varsayılan değer nasıl atanır gördük
 
# return anahtar kelimesi
def topla(x,y):
    print(x + y)
    return x + y                        # sonucu yazdırabilmek için returnu fonksiyonun içine ekledim. Return anahtar kelimesi bize phytonun herhangi bir değer geri döndürmesi anlamına gelir. 
sonuc = topla(3,8)                      #11 yazdı. ben bu 11' başka bir yerde kullanmak için yeniden döndürmek istesem
print(sonuc) 

# başka bir örnek yapalım
def ortalama_hesapla(x,y):
    return (x + y) / 2
ortalama_hesapla(3,7)                   # phyton bu veriyi fiziksel olarak hesapladı, ama sonuc yazdırmadı, çünkü fonksiyona print eklemedim,ama return ile veriyi tutuyor.
print(type(ortalama_hesapla))           #>><class 'function'>
print(type(ortalama_hesapla(2,6)))      #>><class 'float'> : yani bir ondalıklı sayı olduğunu söylüyor, yani fonksiyon çalıştırıldı
# bunu söyle kullabiliriz
a = ortalama_hesapla(2,6)
b = ortalama_hesapla(6,10)
print(a + b)                            #12 : yani a ve b arka planda bir değer döndürdü
#return ifadesi fonk. elde ettiğimiz sonucu bir değişkene atamak istediğimizde kullanırız.

# büyük harfe çevir örneğini bir de return kullanarak yapalım.
def buyuk_harfe_cevir(metin):
    return metin.upper()                #metini bize büyük olarak geri döndürecek
a = buyuk_harfe_cevir("AsDfG")
print(a)                                #>>ASDFG

fonk = buyuk_harfe_cevir
sonuc = fonk("HukonSD")
print(sonuc)                            #HUKONSD: gördüğün gibi fonksiyonlar da phytondaki diğer veri tipleri gibi herhangi bir değişkene eşitlenebilir.

# artık phytonda bir çok şey yapabilecek hale geldiniz. size bir şey bilmiyorum gibi gelebilir ama teorikte öğrendik. Sadece tekrar ve alıştırma yaparak el alışkanlığı kazanabilirsiniz.
# project ögeler videolarına bakarsanız oradaki çözümlü olan 40 problemi özebilirsiniz. oradaki videoları izlerseniz kendinize çok şey katacaksınız diye düşünüyorum.
