# tarih ve zaman ile ilgili fonksiyonları içerir. yolun bolca kesişecek
# date
from datetime import date
bugun = date.today()
print(bugun)                    #2022-02-11
print(type(bugun))              #<class 'datetime.date'> : bu bir sınıf. içinde fonkisyonlar. var aşağıdaki gibi kullanabilirsin.
print(bugun.day)                #11 
print(bugun.month)              #2
print(bugun.year)               #2022
print(bugun.weekday())          #4 : bu gün cuma, 5 yerine 4 yazdı. index mangığı ile sıfırdan başlar
print(bugun.isoweekday())       #5 : 1 den başlar

#başka bir tarih alalım
from datetime import date
gecmis_tarih = date(2015,8,13)
print(gecmis_tarih)             # 2015-08-13
# veriyi alıp üzerinden kaç gün geçtiğini vs bulabilirsin ör
print(gecmis_tarih.weekday())   # 3 >>o gün haftanın 3. günü imiş

gecen_zaman = bugun - gecmis_tarih
print(gecen_zaman)              #2374 days, 0:00:00
print(type(gecen_zaman))        #<class 'datetime.timedelta'> : timetelta sınıfından bir veri . sıradan bir veri değil. kendi için fonksiyonları var

# istediğimiz tarihi el ile girebiliyoruz yani

from datetime import datetime

suan = datetime.now()
print(suan)                     #2022-02-11 15:09:37.092431>>saat bilgisini de verdi
print(type(suan))               #<class 'datetime.datetime'> datetime snıfından bir nesne, kendi içinde fonksiyonları var. bakalım
print(suan.year)                #2022
print(suan.month)               #2
print(suan.day)                 #11
print(suan.hour)                #15
print(suan.minute)              #12
print(suan.second)              #3

# datetime de de date deki fonksiyonlarımın hepsi çalışıyor
#başka neler kullanabilirim?
from datetime import datetime
suan = datetime.now()
#print(datetime.ctime())         # Error! : ctime hangi tarih saat bilgisini göstereceğini bilmiyor
print(suan.ctime())             #Fri Feb 11 15:15:23 2022
print(suan.date())              #2022-02-11
print(suan.time())              #15:17:51.761827
print(suan.date().month)        #2 >> şu an değikeninin içindeki tarihi aldım, o tarihten de ay bilgisini aldım.

# yani fonksiyonlarımız bir öncekine oldukça benziyor.

from datetime import datetime
suan = datetime.now()

gecmis_an = datetime(2014,5,26,6,45,32,123)
print(suan - gecmis_an)         #2818 days, 8:37:24.718850
# datetimedeki fonksiyonların kullanımı ile datedeki fonkisyonların kullanımı aynı gibi.

#zamanı istediğimiz formatta yazdırmak
from datetime import datetime
bugun = datetime.today()
suan = datetime.now()
print(bugun.strftime("%d:%m:%Y"))   #11:02:2022
print(suan.strftime("%d-%m-%Y"))    #11:02:2022
# yani strf time bu gün değişkeninin içinden çağırıldığı için bu gün bilgisine sahip, siz sadece istediğiniz formatı seçiyorsunuz.
# direkt olarak datetime içinden yazsaydım şöyle yazardım
print(datetime.strftime(bugun, "%d:%d:%Y"))
# bir tarih ve parametre aldı.

# timedelta: zamandaki değişim demek
from datetime import datetime
from datetime import timedelta
suan = datetime.now()
tdelta = timedelta(days=7, hours=5, seconds=69)
print(suan + tdelta)            #2022-02-18 20:34:13.773960 >> bulunduğum zamandan belirttiğim zaman geçerse ne olacağını yazdırır
print(suan - tdelta)            #2022-02-04 10:31:55.773960 >> bulunduğum zamandan belirttiğim zaman kadar öncesini ekrana yazdırır.

# biraz modüller ile işledikten sonra odya işlemleri ve oop ile ilgileneceğiz.
# bol bol tekrar yapmayı unutmayın
