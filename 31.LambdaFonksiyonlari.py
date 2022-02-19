# lambda ifadeleri(fonksiyonları)
# ismi olmayan fonksiyonlar oluşturmamıza yarıyor
# nasıl kullanılır?

def kare_al(x):
    return x * x 
print(kare_al(5))       #25

# şimdi aynı fonksiyonu lambda ifadesi ile oluşturalım
# labmda bir fonksiyon tanımlayacağım anlamına geliyor.
# ":"' den önceki kısım fonksiyonun aldığı parametre oluyor. ":"'den sonraki kısım ise fonksiyonun geri döndüreceği değer oluyor. 
# yani bu fonksiyon parametre olarak x'i alıyor ve ve x*x'i geri döndürüyor
kare_al = lambda x : x * x 
print(kare_al(4))       #16

# bir tane daha yapalım
kup_al = lambda x : x ** 3
print(kup_al(9))        #729

# bir değil de iki adet parametre alan bir fonksiyon yazalım
toplam = lambda x, y : x + y
print(toplam(9,9))      #18 
# normal fonksiyonları tanımlarken yaptığım şeye oldukça benziyor.

# bazen benim fonksiyonum berlirli olmayan sayıda parametre alıyordu. onu da lambda ile yazalım
genel_toplam = lambda *args : sum(args)     # bunun bir demet olduğunu unutma
print(genel_toplam(2,3,4,5,6))              #20
# gördüğün gibi fonksiyonlardaki *args kavramı burada da olduğu gibi geçerli.

# lambda'yı herhangi bir değişkene atamadan da kullanabilirim:
print(lambda x,y,z : x * y + z)             #<function <lambda> at 0x00000092C048F040> : bunun bir fonksiyon olduğunu yazdı
print((lambda x,y,z : x * y + z)(3,5,6))    #21>> bunu bu şekilde bir değişkene atamadan kullanabilirsin.
print((lambda *args :sum(args) / len(args))(2,3,4,5,6,7,8,9))   #5.5
# yani biz lambda fonksiyonlarını herhangi bir isim vermeden de anonim olarak kullanabiliyoruz.

# peki ne işimize yarar?
# >fonksiyonları lambda ile ifade etmek daha kısa
# >programımızda bir fonksiyonu sadece bir yerde kullanacaksak, onun için ayrı fonk. ismi oluşturup sürekli yer işgal etmesine gerek yok. kullanıp atıcaksak onu bir lambda ile yazmak daha mantıklı
# >ama programın farkl yerlerinde aynı fonk. defalarca çağırıcaksan fonksiyonu def anahtar kelimesi ile oluşturusun, sürekli orada var olmayı sürdürür.
# > asıl önemli olan kısmı, bazı fonksiyonlar parametre olarak fonksiyon istiyorlar. onlarda çok fazla kullanacağız.

liste = [("Ali",20),("Veli",19),("Emel",30),("Hakan",24)]
liste.sort()        #Sırala
print(liste)        #[('Ali', 20), ('Emel', 30), ('Hakan', 24), ('Veli', 19)]: birinci bileşenlere göre, yani isme göre sıralamış

# biz bunu ikinci bileşenlere, yani yaşlara göre sıralamak isteseydik nasıl yapacaktık?
liste = [("Ali",20),("Veli",19),("Emel",30),("Hakan",24)]
liste.sort(key= lambda x : x[1])        #key bizden fonksiyon istiyor.
print(liste)        #[('Veli', 19), ('Ali', 20), ('Hakan', 24), ('Emel', 30)]

# bunu şöyle de yapabilirdim:
liste = [("Ali",20),("Veli",19),("Emel",30),("Hakan",24)]
def yaslari_goster(x):
    return x[1]
liste.sort(key= yaslari_goster) 
print(liste)        #[('Veli', 19), ('Ali', 20), ('Hakan', 24), ('Emel', 30)]
# aynı sonucu verdi. ama burada bu fonksiyonu bu şekilde ifade etmemin bir manası yok çünkü bunu bir daha kullanmayacağım. sadece bir kere kullanacağım için lambda ile yapmak daha mantıklıdır.
# burada biz demetlerden oluşan bir listeyi sıraladık

# diyelim ki liste 2 de sözlükler olsun. liste 2 'yi sıralamak istiyorum ama neye göre sıralayacağım
liste2 = [{"Ad":"Ahmet","Soyad":"Calışkan","Yaş":25},{"Ad":"Mehmet","Soyad":"Uzun","Yaş":22},{"Ad":"Duru","Soyad":"Yıldız","Yaş":24}]
liste2.sort(key= lambda x: x["Soyad"])      #Hatırla, sözlükler key'lere göre sıralanıyordu
print(liste2)       #[{'Ad': 'Ahmet', 'Soyad': 'Cal��kan', 'Ya�': 25}, {'Ad': 'Mehmet', 'Soyad': 'Uzun', 'Ya�': 22}, {'Ad': 'Duru', 'Soyad': 'Y�ld�z', 'Ya�': 24}]
# yaşa göre sıralamak istersem:
liste2.sort(key= lambda x: x["Yaş"])      
print(liste2)       #[{'Ad': 'Mehmet', 'Soyad': 'Uzun', 'Ya�': 22}, {'Ad': 'Duru', 'Soyad': 'Y�ld�z', 'Ya�': 24}, {'Ad': 'Ahmet', 'Soyad': 'Cal��kan', 'Ya�': 25}]
# bu şekilde de sözlüklerden oluşan bir listeyi sıralayabildik

#kısaca tekrar edelim. lambda ifadesi tek satırda fonk. oluşturmaya yarıyor. 2 avantajı var. sık kullanılmayan fonk. için idealdir. yer işgal etmez.
# ikinci avantajı ise bir çok fonksiyon parametre olarak fonksiyon oluyor. öyle bir durumda bize yazım kolaylığı sağlıyor. uzun uzun fonksiyon tanımlamama gerek kalmıyor.
# kodum bu sadece temiz ve kısa oluyor
# map, filter ve reduce fonksiyonlarını kullanırken işimize çok işe yarayacak.
