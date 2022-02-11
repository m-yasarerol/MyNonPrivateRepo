# bu gün öğreneceğimiz kavramlar çok önemli, sayısal veri tipleri.
# intgregerler tam saylara karşılık gelirken, float veri tipleri ondalıklı sayıları ifade eder.
# phytonda böyle bir özellik var, siz bir değişken tanımladığınız zaman phyton onun veri tipini otomatik olarak tanıyor örneğin aşağıdaki veri tipinin integer olduğunu belirtmene gerek yok.
from typing import runtime_checkable
from typing_extensions import runtime


sayi = 5
sayi2 = 3.5
print(sayi)

# acaba gerçekten yukarıdaki verinin tam sayı olduğunu anladı mı? nasıl emin olabilirim?
#cevap böyle durumlar için phyton'da "type" fonksiyonunu kullanırız
print(type(sayi))
#gördüğünüz gibi tanıdı. cevap: "<class 'int'>"

print(type(sayi2))
#dönüt:<class 'float'>

# kısaca siz herhangi değişken oluşturup bir değer atadığında, onun tipini ekstradan belirtmene gerek yok. phyton zaten onun içindeki değere bakıp ne olduğunu anlıyor ve ona göre işlem yapıyor.
# dediğim gibi 2 adet ana veri tipimiz var.
# tam sayı olanlar: integer 
# ondalıklı olanlar : float veri tipidir.

sayi3 = 5**2
print(sayi3)
#gördüğün gibi 5^2 şeklinde değişken atadığımda phyton sonucu hesaplayıp yazdırıyor.
#dönüt: 25

sayi4 = 5 / 2
print(sayi4)
# yukarıdaki özellik float veri tipi için de geçerli
# dönüt: 2.5

#   MATEMATİKSEL İŞLEMLER
# Toplama         " + "
# Çıkarma         " - "
# Çarpma          " * "
# Bölme           " / "
# Tamsayı bölmesi "// "
# Kuvvet alma     "** "
# Mutlak değer    "abs"
# Yuvarlama       "round"
# İşlem önceliği

print(3 + 4)    #dönüt:7
print(3 - 4)    #dönüt:-1
print(3 * 4)    #dönüt:12
print(16 / 5)   #dönüt:3.2
print(16 // 5)  #dönüt:3 (sadece tam sayı tarafını gösterir, virgülden sonrasını göstermez)
print(3 ** 4)   #dönüt:81 (3^4)
print(abs(-2))  #dönüt:2
print(abs(-2.16))#dönüt:2,16 (gördüğün gibii "abs" fonksiyonu içine hem integer hem float tipinde veri tipi alabilir.)

sayi5 = 22 / 7  #dönüt:3.142857142857143
sayi5 = 22 / 7
print(round(sayi5)) #dönüt:3 (gördüğün gibi sayıyı 3'e yuvarladı.)

sayi6 = 3.51566
print(round(sayi6))#dönüt:4 (gördüğün gibi hangi sayıya daha yakınsa o sayıya yuvarlıyor.)

#peki ya virgülden sonra 3 basamak almak istersek? o zaman round fonksiyonuna ikinci bir parametre girmemiz gekekir. ÖR:
sayi6 = 3.51566
print(round(sayi6,2)) #dönüt: 3,52 gördüğün gibi virgülden sonra 2. basamağa kadar yuvarladı.

#   PHYTONDA İŞLEM ÖNCELİĞİ
# işlem önceliği günlük hayatta kağıt kalem ile yaptığımız hesaplamalardaki işlem önceliğinden farklı değil.
# yani önce parantezler,çarpma bölme,toplama çıkarma şeklinde ilerler.
print(3 * 5 + 6) #dönüt:21(önce çarpma işlemini yaptı)
print((3 + 2) * 4 + 3) #dönüt:23
#matematiksel işlemleri çok çok fazla kullanacaksınız, bunlar olmadan işlem yapmanız çok mümkün değil. o nedenle bol bol tekrar etmekte fayda var. İlk kez öğreniyorsanız temeli sağlam atmanızı tavsiye ederim.

#sayılar konusunda sıkça karşılaşacağınız bir diğer konu da sayıları karşılaştırma Ör: büyüklük , küçüklük, eşitlik vb.
#   KAŞILAŞTIRMA OPERATÖRLERİ
# Eşittir         " =="
# Küçüktür        " < "
# Büyüktür        " > "
# Küçük eşittir   " <="
# Büyük eşittir   " >="
# Eşit değildir   " ! "

print(3 == 3)   #dönüt: true (bu, bollian denilen bir veri tipidir. doğru ya da yanlış alır. burada dikkat etmen gereken şey 3 adet eşittir var.)
sayi7 = 3 == 3
print(sayi7) #dönüt:true

sayi8 = 4
print(sayi8 = sayi8) #error!

sayi8 = 4
print(sayi8 == sayi8) #dönüt:true

print(3 == 5)   #dönüt:false

sayi10 = 5
sayi11 = 6
print(sayi10 > sayi11) #dönüt:false
print(sayi10 < sayi11) #dönüt:true
print(sayi10 == sayi11) #dönüt:false
print(sayi10 != sayi11) #dönüt:ture (bu kod şu anlama gelir: "sayi 10 sayi 11'e eşit değil mi? iki değer birbirine eşit olmadığından "true" sonucu döndürülür.)

sayi12 = 10
sayi13 = 10
print(sayi12 >= sayi13) #dönüt: true (bu kod şu anlama gelir: "sayi 12 sayı 13'den büyüktür, eşittir." bu iki say birbirine eşit olduğundan "true" sonucu döndürülür)

a = 1
b = a
a = 5
print(b) 
# soru, b sayısını yazdırdığımda 1 mi yazacak, 5 mi yazacak?
# benim yanıtım: 1 yazdırır, çünkü phyton satır satır ilerler.
# sonuç: 1
# ben a = 1 dediğimde  bellekte a kutusu oluşturup içine 1 koyuyorum, 
# b = a dediğim zaman bellekte bir b kutusu oluşturup a nın içindeki değeri (1) koyuyorum.
# a = 5 dediğimde a kutusundaki sayıyı 5 yapıyorum, benim a kutusundaki sayıyı değiştirmem, b konusuna attığım 1 i etkilemez. Bu mantığı unutma lütfen, oldukça önemli.

# sayıları karlışaltırmayı da öğrendik, şimdi stringleri ve integerleri birbirine çevirmeye çalışalım.
sayi14 = "100"
sayi15 = 100
print(type(sayi14)) #dönüt:<class 'str'>
print(type(sayi15)) #dönüt:<class 'int'>

sayi14 = "100"
sayi15 = 100
print(sayi14 == sayi15)
# #soru2: sayi14 string veri tipindedir, sayi15 integer veri tipindedir. fakat ikisinin de değeri "100" dür. Phyton bu iki sayıyı eşit olarak mı kabul edecektir. Yukardaki kodun çıktısı nedir?
# A) True
# B) False
#cevap : false, çünkü ilk 100 metin şeklindedir, phython için herhangi bir sayısal büyüklük ifade etmez

sayi14 = "100"
sayi15 = 100
sayi16 = int(sayi14) # int fonksiyonu, integer'e çevrilebilecek değerleri integere çveirir.
print(sayi15 == sayi16) #dönüt: true
#yani yazdığın string integer çevrilebilecek bir string ise, onu int fonksiyonun içine yazdığında tam sayıya çevirecektir.

sayi14 = "100asd"
sayi15 = 100
sayi16 = int(sayi14)
print(sayi15 == sayi16) #dönüt:ValueError: invalid literal for int() with base 10: '100asd'
# yani phyton bize kızdı. Stringe çevrilemeyecek bir ifadeyi stringe çeviremezsin dedi.

sayi17 = int(3.9)
print(sayi17)
#soru 3, yukarıdaki kod hata verecek mi yoksa vermeyecek mi?
# dönüt: 3  gördüğün gibi integer fonksiyonu round gibi bir yuvarlama yapmıyor. direkt olarak ondalık kısmı görmezden geliyor. Round ile kullansaydık 4 sonucunu alırdık.

# string ifadeyi integere çevirebildiğimiz gibi, integer bir veriyi stringe de çevirebiliriz.
sayi18 = 123
sayi19 = str(sayi18) #içine girilen ifadeyi stringe çeviren bir fonksiyondur.
print(sayi19)  # dönüt:123
print(type(sayi19)) #dönüt:<class 'str'>
print(type(sayi18)) #dönüt:<class 'int'>

#ve bu gün işleyeceğimiz son şey, eğer bir integer ile çalışıyorsan, özellikle while döngüsünde sürekli olarak bu verileri değiştirmen gerekebilir. mesela her sefferinde i'yi arttrmak istiyoruz.
i = 1
i = i + 2
print(i) #dönüt:3

i = 1
i  += 2
print(i) #dönüt:3 # aynı sonucu verdi, genelde bu yapı kullanılır.

i = 3
i *= 5
print(i) #dönüt:15 (i sayısını 5 ile çarp ver i' ye eşitle anlamına geliyor. yani bu ikisini birlikte yapar.)
#bu bütün işlemler için geçerlidir. yani:
i = 30
i /= 7
print(i) #dönüt:4.285714285714286 (burada da i sayısını(30) 7'ye böldük ve o değeri i' ye atadık.)

i = 30
i //= 7
print(i) #dönüt: 4 (gördüğün gibi tam bölmeyi kullanırsan tam olarak böler.)

#bu günlük dersimizin sonuna geldik, özetlersek:
#1)temel sayı tiplerini tanıdık. iki taneydi zaten tam sayı ve ondalık sayılar.
#2) bu sayılar ile yapılabilecek matematiksel işlemleri inceledik ve işlem önceliğinden bahsettik
#3) bu sayıları nasıl karşılaştırabileceğimizi gördük
#4) sayıları birbirine çevirdik ve sayılarımızı nasl arttırabiliriz ve azaltabiliriz bunun üzerine konuştuk
# LÜTFEN BUNLARI ÇOK İYİ VE ÇOK İYİ TEKRAR EDİN  ŞU HALEN VERİ TİPLERİNDEYİZ, HALEN YAPABİLECEĞİNİZ ŞEYLER ÇOK FAZLA DEĞİL, 2-3 VİDE SONRA KONTROL YAPILARI, İF BLOKLARI VE DÖNGÜLERİ İŞLEDİKTEN SONRA BİR SÜRÜ UYGULAMA İMKANI BULACAKSINIZ.
# BU BİLGİLERLE PROJELER YAZACAĞIZ, O NEDENLE LÜTFEN SABREDİN VE TEMELİNİZİ SAĞLAM ATIN. KENDİNİZE ZAMAN AYIRIN VE BUNLARI İYİ PEKİŞTİRİN, BU SAYEDE DAHA SAĞLIKLI ŞEKİLDE İLERLEYEBİLİRİZ.









