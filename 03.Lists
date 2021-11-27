# listeler nedir ve nasıl oluşturulur? 
# liseler nasıl yazdırılır?
# len fonksiyonu nedir
# liste elemanlarına nasıl erişilebilir?
# liste nasıl parçalanır?
# listeler phytonda verilerimi sıralı bir şekilde hafızada dpolamamıza yarayan bir veri yapısıdır. Çok sık kullanılan bir veri yapısıdır. o nedenle çok önemli

#bir liste nasıl oluşturulur?
#köşeli parantez olması, değişkenimizin bir liste olduğunu ifade eder.

from _typeshed import OpenTextModeReading
from typing import runtime_checkable


renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(type(renkler))    #<class 'list'>
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il']
#bildiğin gibi print fonksiyonu içine verdiğin veriyi ekrana yazdırmaya yarar.

#stringler de aslında karakterlerden oluşan bir listedir
#len fonksiyonu: bize stringin uzunluğunu söylüyordu.
print(len(renkler))     #5 (listemizde 5 adet eleman var)

#peki, listemizin elemanlarına nasıl ulaşabiliriz? stringlerde olduğu gibi index vasıtasıyla elemanlarımıza ulaşacağız Ör:
print(renkler[1])       #beyaz

print(renkler[6])       #error! (5 eleman var)

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler[2:])      #['sar�', 'mavi', 'ye�il']

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler[1:4])      #['beyaz', 'sar�', 'mavi'] (gördüğüm gibi 1. indeksi yazdırdı, 4. indeksi yazdırmadı. ikinci sınırı dahil etmediğini söylemiştik.)

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler[::2])      #['siyah', 'sar�', 'ye�il'](ikişer ikişer arttı.)
#yukarıdaki kodun algoritması şu şekildedir: print(renkler[{başlangıç intex} {bitiş index} {index artış kat sayısı}])

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler[1:4:2])      #['beyaz', 'mavi'] (1'den 4'e kadar 2'şer 2'şer yazdırdı.)


# append metodu : sonuna
# insert metodu : araya
# remove komutu : çıkart
# extend        : birden fazla eleman ekle
# pop metodu    : bir listenin en son elemanını siler ve sana geri döndürür.
# reverse metodu : listeyi tersinden sıralar/tersine döndürür
# sort ve sorted metotları : sort sıralar
# bu metotlar listemizi değiştirmek için kullanacağımız metotlardır

#appent metodu listemizin sonuna eleman eklememizi sağlar.
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il']
renkler.append("gri")
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il', 'gri']

#peki ya ben elemanı en sona eklemek istemiyorsam, aralara bir yere eklemek istiyorsam?
#işte bu noktada da insert metoduna başvuracağız. (önce kaçıncı instekse eklemek istediğimi, sonra ne eklemek istediğimi belirtmeliyim.)
renkler1= ["turuncu", "ela", "eflatun"]
print(renkler1)         #['turuncu', 'ela', 'eflatun']
renkler1.insert(0,"mor")
print(renkler1)         #['mor', 'turuncu', 'ela', 'eflatun']
#yani 0. intexe gri geldiği zaman diğerlerinin sırası +1 sağa kaydı.
#bu şekilde appent ile sonuna eklerken, insert ile araya herhangi bir yere eleman ekleyebilirim.

#remove metodu, bir listeleden bir elemanı silmeye yarar. kullanımı:
renkler1= ["turuncu", "ela", "eflatun"]
print(renkler1)         #['turuncu', 'ela', 'eflatun']
renkler1.remove("ela")
print(renkler1)         #['turuncu', 'eflatun']

#listeye birden fazla eleman eklemek istediğimizde extend metodu kullanabiliriz.
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
renkler11 = ["kırmızı", "bej"]
renkler12 = ["kehribar", "italik"]
renkler.append(renkler11)
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il', ['k�rm�z�', 'bej']] >> gördüğün gibi 2. listeyi direkt olduğu gibi ekledi. kırmızı ve bej'i ayrı ayrı eklemedi. listeyi olduğu gibi ekledi, 
# eğer ben tek teker teker listenin kendisini değil de listenin elemanlarını eklemek istersem orda da extend metodunu kullanacağım. ÖR:
renkler11.extend(renkler12)
print(renkler11)        #['k�rm�z�', 'bej', 'kehribar', 'italik'] >>gördüğün gibi elemanları ayrı ayrı ekledi.

#pop metodu bir listenin en son elemanını siler, silmekle de kalmaz o elemanı size geri döndürür. kullanımı:
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il']
renkler.pop()
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi']

#ayrıca bu metot geriye bir geri dönüş yapan bir fonksiyondur, yani siz bu fonksiyonu bir değişkene atayıp, silinen instexleri ekrana yazdırabilirsiniz.
#örnek:
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
silinen = renkler.pop()
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi']
print(silinen)          #yeşil

# reverse metodu, listeyi tersinden sıralayan, daha dorusu tersine döndüren bir metottur.
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler)
renkler.reverse()       #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il']
print(renkler)          #['ye�il', 'mavi', 'sar�', 'beyaz', 'siyah']
#şunu fark etmelisiniz ki, reverse kullandığınız zaman, eski listeniz değişiyor. elemanların yerleri değişir, farklı bir liste olur.

#sort metodu, listeyi alfabetik olarak sıralar. eğer içinde metinsel ifadeler varsa alfabetik olarak sıralar, eğer içinde sayısal ifadeler var ise küçükten büyüğe doğru sıralar.
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il']
renkler.sort()
print(renkler)          #['beyaz', 'mavi', 'sar�', 'siyah', 'ye�il']

#peki ya tersten sıralamak istersem?
# A) listemizi sort ile sıralayıp, revers ile tersten sıralayabiliriz
harfler = ["b", "a", "c"]
print(harfler)          #['b', 'a', 'c']
harfler.sort()          
print(harfler)          #['a', 'b', 'c']
harfler.reverse()
print(harfler)          #['c', 'b', 'a']

#B) bu iki adım yerine, listemizi tek seferde de tersten sıralayabiliriz. yine sort metodu kullanacağız ama içine bir parametre gireceğiz.
harfler = ["b", "a", "c"]
harfler.sort(reverse= True)  
print(harfler)          #['c', 'b', 'a'] >> reverse= metodunu kullanıp true atarsan tersten sıralar.
# tekrar ediyorum. bir listeyi sıraladığında listen eski halini kaybeder, başka bir liste olur, eğer listeni bozmak istemiyorsan ancak sıralanmış haline de ihtiyacın varsa, bu noktada sorted metodunu kullanıyoruz.

#ör: renker kümesinin sıralanmış halini istiyorum ama bu listenin de bozulmasını istemiyorum:
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il'] >> listemin kendisi, srıalanmış değil, karışık sırada.
renklers = sorted(renkler) 
print(renklers)         #['beyaz', 'mavi', 'sar�', 'siyah', 'ye�il'] >> liste 2 oluşturuldu, renkler listesinin  sıralı hali.
print(renkler)          #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il'] >> gördüğün gibi renkler listesine bir şey olmadı. 

# yani, bir listeyi sıralı halde istiyorsan ancak yapısının bozulmasını istemiyorsan, sorted metodu iyi bir seçim olacaktır.

# min, max ve in kullanımı
# sum ve kullanımı      :toplam alır
# for döngüsü ile listeyi yazdırmak
# enumerate
# listeyi stringe çevirmek ve join metodu 
# stringi listeye çevirmek ve split metodu

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]

sayılar = [1,2,3,9,4,3,7,8]
print(min(renkler))     #beyaz >> min metodu bir listede en küçük elemanı alır, eğer liste alfabetik ise alfabetik olarak en küçük elemanı alır
print(min(sayılar))     #1
print(max(sayılar))     #9
print(max(renkler))     #yeşil >> alfabetik olarak en ilerideki değeri seçti.
# yani min ve max en küçük ve en büyük elemanları döndürür.

#sum toplam fonksiyonudur.
print(sum(sayılar))     #37
print(sum(renkler))     #error! >> sum fonksiyonuna gönderdiğimiz liste stringlerden oluşamadı

#for döngüsü ile listeyi yazdıralım. döngü olmadan phyton olmaz. 
#listenin elemanlarını nasıl teker teker yazdırabiliriz?
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
for renk in renkler:
    print(renk)         #siyah
                        # beyaz
                        # sar�
                        # mavi
                        # ye�il
# arka planda şu oluyor: fonksiyon diyor ki, "renk", "renkler" listesinin içinde gezinsin.
# bu arada "renk" yazmak zorunda değiliz, "i" de diyebilirdik, ör:ü
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
for i in renkler:
    print(i)            #siyah
                        # beyaz
                        # sar�
                        # mavi
                        # ye�il
# #mantık şöyle işliyor, "i" ilk önce:
# 1) siyahın yerine geçer ve siyahı yazdırır.
# 2) beyazın yerine geçer ve beyazı yazdırır.
# 3) sarının yerine geçer ve sarıyı yazdırır.
# 4) mavinin yerine geçer ve maviyi yazdırır.
# 5) yeşilin yerine geçer ve yeşili yazdırır.
# 7) bütün elemanlarına yerine teker teker geçtikten sonra döngüyü bitirir. for döngüsü çok önemli, bu konuyu tek bir videoda işleyeceğiz.

#enumerate fonksiyonu bir listeyi numaralandırmamızı sağlar. Ör:
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(list(enumerate(renkler))) #[(0, 'siyah'), (1, 'beyaz'), (2, 'sar�'), (3, 'mavi'), (4, 'ye�il')]
# ancak eğer siz numaralandırma işinin sıfırdan başlamasını istemiyorsanız:
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print(list(enumerate(renkler, start=3))) #[(3, 'siyah'), (4, 'beyaz'), (5, 'sar�'), (6, 'mavi'), (7, 'ye�il')]
# numaralandırmaya 3'ten başladı.

# in kullanımı: liste elemanlarını kontrol etmemizi sağlar
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print("siyah" in renkler)   #true 
#yukarıdaki kod şu anlama gelir; "siyah", renkler listesinde var mı?
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
print("gri" in renkler)   #false
# yani biz bir elemanın listede olup olmadığını kontrol ederken, in anahtar kelimesini kullanabiliriz.

#  ÖNEMLİ OLAN 2 NOKTA VAR
# 1)listeyi stringe çevirmek
#yani, aşağıdaki listeyi tek bir metin dosyası haline çevirmek istersem,
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = "".join(renkler)
print(stringrenkler)    #siyahbeyazsar�maviye�il

# zaten join birleştirmek, bağlamak anlamına gelir, neden bitişik halde birleştirdi, çünkü tırnakların arasında boşluk bırakmadım, hadi bırakalım.
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = " ".join(renkler)
print(stringrenkler)    #siyah beyaz sar� mavi ye�il

#arasına virgül koyalım
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = ", ".join(renkler)
print(stringrenkler)    #siyah, beyaz, sar�, mavi, ye�il

#mantık şöyle işliyor, listedeki elemanları birleştir, aralarına da parantez içindeki elemanı koy.

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = "-".join(renkler)
print(stringrenkler)    #siyah-beyaz-sar�-mavi-ye�il
print(type(stringrenkler))  #<class 'str'>

#2) belirli bir karakteri bölüp listeye çevirmek (çok önemli, verileri yapılandırmak?)
#   YANİ STRİNGİ LİSTEYE ÇEVİRMEK
# SPLİT METODU İLE YAPABİLİRİZ!
# renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = "-".join(renkler)
print(stringrenkler)    #siyah-beyaz-sar�-mavi-ye�il
# örnek: yukarıdaki ifadeyi tirelere göre böl ve her bir elemanı bir listeye atayacağım.

renkler2 = stringrenkler.split("-")
print(renkler2)         #['siyah', 'beyaz', 'sar�', 'mavi', 'ye�il']

# KENDİME NOT: Ali hoca derste yapılandırılmamış, string ifadelerden oluşan büyük bir veriyi nasıl yapılandırabileceğimizi sormuştu, peki ya sorunun cevabı split metodu ise..?
#kenime ödev, metin olarak ard arda yazılmış hastalıklarla ilgili bir dosyayı split metodu ile liste durumuna çevir, alfabetik olarak sırala, listedeki eleman sayısını yazdır.

#split tek birden fazla eleman alabilir. Ör:
renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = "-".join(renkler)
print(stringrenkler)
renkler2 = stringrenkler.split("ma")
print(renkler2)         #['siyah-beyaz-sar�-', 'vi-ye�il'] >> gördüğün gibi "ma" dan öncesini bir eleman, sonrasını bir eleman olarak aldı

renkler = ["siyah", "beyaz", "sarı", "mavi", "yeşil"]
stringrenkler = " - ".join(renkler)
print(stringrenkler)
renkler2 = stringrenkler.split(" -")
print(renkler2)         #['siyah', ' beyaz', ' sar�', ' mavi', ' ye�il'] >> boşluklara dikkat :) boşlukları da aldı.

# bu ders çok önemliydi, liste kullanmadığın hiçbir program olmayacak, dikkatli izle, tekrar yap, kodu değiştirip tekrar dene
# bir sonraki videoda demetleri , kümeleri ve sözlük yapılarını incelicez ve temel veri yapılarını bitirmiş olucaz, sonrasında işin eğlenceli kısmına geçicez. yani kontrol mekanizmalarına if bloklarına ve döngülere geçeceğiz. sonrasında eğlenceli uygulamalar yapacağız.
