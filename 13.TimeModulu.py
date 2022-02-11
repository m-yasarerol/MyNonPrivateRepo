# önemli modülleri incelemeye devam
# time modülü: bize zamanla ilgili fonkisyonları sağlar
import time 
zaman = time.time()
print(zaman)

#time fonisyonu: geçerli zamanın saniye cinsinden değeri. 1 ocak 1970 den beri geçen zamanın saniye cinsinden değeri
#bu fonk. oldukça önemli. yaygın olan kullanımı:

import time
baslangic = time.time()
liste = []                          # boş bir liste
for i in range(1000000):            # 1 milyona kadar
    liste.append(i)                 # .. olan sayıları listeye ekle
bitis = time.time()                     
print(bitis - baslangic)            #Output: 1.1850686073303223
# ne yaptım? programın başlangıc zamanını bir yerler not ettim, sonrasında bitiş zamanını bir yerlere not ettim. böylece porgramın çalışma süresini yazdırdım.
# yani bir işi yapacaksanız ve elinizde iki tane algoritma var ise, işlerin sürelerini time.time() fonksiyonu ile karşılaştrabilirsin. Önemli!
 
# 2. fonk. : ctime(): içime hiçbir şey yazmazsan şu anki tarihi verir.
import time
zaman = time.ctime()
print(zaman)                        #Fri Feb 11 13:51:30 2022

# parametreye bir değer girersem:
import time
zaman = time.ctime(10000)
print(zaman)                        
# başlangıç tarihinfen 10.000 saniye geçerse tarihin ne olduğunu döndürür
# veri tipi "int"

# bir sonraki fonk. localtime(): zamanın değişik bileşenlerini ayrı ayrı yazar. çok kullanışlı değil. yine de görelim
import time
zaman = time.localtime()
print(zaman)                        # >>time.struct_time(tm_year=2022, tm_mon=2, tm_mday=11, tm_hour=13, tm_min=55, tm_sec=0, tm_wday=4, tm_yday=42, tm_isdst=0)

# içine bir sayı yazarsan aynı şekilde başlangıç tarihinden verdiğin saniye kadar sonrasını aynı formatta verir.

# asctime(): eğer içine hiçbirşey yazmazsan ctime()'nin aynısı olur. ama onun içine parametre olarak localtime() verirsen onu tekrardan okuyabileceğin formata çevirir
zaman2 = time.asctime(zaman)
print(zaman2)                       #>>Fri Feb 11 13:57:59 2022: bir önceki örnekteki karışık olarak verilen tarihin okunur bişimde verilmesi.
# local time'i çok fazla kullanmıyorsan asctime 'yi de kullanmazsın. 
#nerde kullanırız? zaman verisini bir yerden çekiyoruzdur. oradaki veri localtime formatında geliyordur. orada asc time 'i kullanabiliriz.

# EN ÇOK KULLANACAĞINI DÜŞÜNDÜĞÜM FONKSİYON
#STRFTİME()
import time
zaman = time.strftime("%d:%m:%Y")
print(zaman)                        #11:02:2022
#buna saat dakika ve saniyeleri de ekleyelim.
import time
zaman = time.strftime("%d:%m:%Y %H:%M:%S")
print(zaman)                        #11:02:2022 14:04:21
# strf time zaman formatlarını ayrı olarak yazacağım. çünkü kütüphanede bulamadım. oysa ki hocanın anlattğı eğitimde var. eğitim 1 yıl önce yazılmış . kütüphane güncellenmiş olabilir.

# dolayısıyla şimdiye kadar kullandıklarımız içinde en kullanışlısı strf time dir. ama dediğim gibi veriyi herhangi bir yerden çekiyorsanız oradaki veri size timetufle olarak gelebilir.
# hangi formatta zaman tutmak istiyorsan ona göre parametre verebilirsin.
# en çok kullanacağımız strf time , yani formatlayabildiğimiz içerikti.

#time.sleep(): içine yazdığın değer saniye cinsinden bir değişken, kodun belirli bir süre uyumasını sağlar. bu da çok önemli. mesela selenium ile bir web sitesindeki değişik sayfalarda otomatik olarak bir şeyler yapmasını istiyorsun. sayfaya girdiğinde aynı anda yüklenmeyeceği için aynı anda giriş yap butonuna basarsa hata verebilir. sayfanın yüklenmesini bekleyemek isteyebilirsin.
import time
print("Program başladı")
time.sleep(3)
print("Program sonlandı")           # Program ba�lad�
                                    # (arada 3 saniye bekledi)
                                    # Program sonland�
# sleep fonk önemliydi. temel fonksiyonları işledik. bunlarla bir çok şey yapabilirsiniz.
#modüllerden devam edeceğiz. datetime modülü ile.
