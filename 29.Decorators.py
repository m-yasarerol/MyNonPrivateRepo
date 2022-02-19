# decorator nedir?
# decorator aslında kendisi  de bir faonksiyondur, ancak şöyle bir işlevi var, bizim var olan fonksiyonumuza özellikler eklememizi sağlıyorlar. 
# mesela programımızda 100 adet fonk. çalışsın, biz de bu 100 fonksiyonun ne kadar sürede işlerini bitirdiğini bilmek isteyelim. eğer bir decoratordan
# faydalanmazsak, bu 100 adet fonksiyona teker teker gidip, her birinin ne kadar süre çalıştığnı gösteren kodları yazmamız gerekir. ancak biz zamanı 
# ölçen bir decorator oluşturursak ve bu fonksiyonları o decorator ile ilişkilendirirsek, o kodu bir kere yazıp tüm fonksiyonlarımızda kullanabiliriz.
# ilk önce bir decoratorun yapısı nasıldır, nasıl işliyor anlamamız gerekiyor. 
# ilk olarak bir fonk. oluşturalım
def decorator(fonk):                    #ismi "decorator" olmak zorunda değil. ancak dıştaki fonk. genelde decorator fonk olarak anılır.
    def wrapper():                      # içerideki fonk genelde wrapper, yani sarıp sarmalayan ismi ile anılır.
        print("Fonksiyon çalışmadan önceki işlemler")
        fonk()
        print("Fonksiyon çalıştıktan sonraki işlemler")
    return wrapper                      # dikkat et, parantezli değil. fonksiyonun kendisini geri döndürdüm.

@decorator                              # fonk. üstüne @decorator yazmam, "bu fonksiyonu al, decoratore gönder" anlamına geliyor
def fonksiyon():
    print("fonksiyon çalışıyor.")

fonksiyon()                             # Fonksiyon �al��madan �nceki i�lemler
                                        # fonksiyon �al���yor.
                                        # Fonksiyon �al��t�ktan sonraki i�lemler

fonksiyon2 = decorator(fonksiyon)       # parantezleri koyup da gönderirseniz, parantezin kendisini değil, fonk. çalıştıktan sonra bir geri dönüş değeri var ise onu göndermiş olursunuz. 
# fonk2 artık aslında wrapper fonksiyonudur
fonksiyon2()                            # Fonksiyon �al��madan �nceki i�lemler
                                        # fonksiyon �al���yor.
                                        # Fonksiyon �al��t�ktan sonraki i�lemler
# kabaca bir decoratorun çalışma prensibi bu şekilde. şimdi biraz daha gerçekçi örnekler ile incelemeye çalışalım

# mesela az önce bahsettiğimiz zaman hesaplama işlemini yapalım
import time
def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):        # çünkü ben bu decoratoru farklı farklı fonksiyonlarda kullanmaya ihtiyaç duyabilirim. Şimdi bu içerideki wrapper fonk. hem bizim fonksiyonumuzu çalıştıracak, ama onun öncesinde başladığı zaman kayıt edecek, fonk. çalışmas bittiğinde de bittiği zamanı kayıt edip ekrana yazdıracak
        baslangic = time.time()         # geçerli zamanı kaydet
        fonk(*args,**kwargs)            # bizim parametre olarak verdiğimiz fonk çalıştıracak
        bitis = time.time()             # bitiş zamanını kayıt et.
        print(f"İşlem: {bitis-baslangic} saniye sürdü.")
    return wrapper
@zaman_hesapla                          # kareleri_al fonksiyonu, otomatik olarak zaman_hesapla fonksiyonuna "fonk" olarak gönderilir
def kareleri_al(liste):                 # buradaki liste, zaman_hesapla fonksiyonundaki "wrapper"' e gönderilir
    for i in liste:
        print(i * i)

@zaman_hesapla                          # kupleri_al fonksiyonu, otomatik olarak zaman_hesapla fonksiyonuna "fonk" olarak gönderilir
def kupleri_al(liste):                  # buradaki liste, zaman_hesapla fonksiyonundaki "wrapper"' e gönderilir
    for i in liste:
        print(i ** 3)

@zaman_hesapla                          # topla fonksiyonu, otomatik olarak zaman_hesapla fonksiyonuna "fonk" olarak gönderilir
def topla(a,b):                         
    time.sleep(1)
    print(a + b)

kareleri_al(range(1000))                #0,1,4,....,998001 ��lem: 0.07600569725036621 saniye s�rd�.
kupleri_al(range(1000))                 #0,1,8,.....,997002999  ��lem: 0.18001580238342285 saniye s�rd�.
topla(10,20)                            #30 ��lem: 1.0177123546600342 saniye s�rd�.
# eğer ben bunların hepsi için zamanın ne kadar sürdüğünü hesaplamak isteseydim, hef fonksiyona teker teker kod yazmam gerekicekti.

# yazdığımız 3 fonksiyon geriye değer döndürmüyor. sadece print ediyor. değer döndürmeyi de uygulamalı olarak görelim. hepsini baştan yapacağız
import time 
def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):
        baslangic = time.time()
        sonuc = fonk(*args,**kwargs)    # yani eğer senin fonksiyonun bir geri dönüş değeri üretiyorsa, yani bir return değeri varsa, bunu wrapper fonksiyonunda kaybetmemek için fonksiyonunuzu çalıştırdığınız yerde bir değişkene atamalısınız.
        bitis = time.time()
        print(f"İşlem {bitis-baslangic} saniye sürdü.")
        return sonuc                    # sonucu geridöndürmeyi unutma.
    return wrapper

@zaman_hesapla
def kareleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i * i)             # bu for döngüsü bittiğinde, tüm elemanların karelerini listeye eklemiş olacağım
    return sonuc

@zaman_hesapla
def kupleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i ** 3)             # bu for döngüsü bittiğinde, tüm elemanların küplerini listeye eklemiş olacağım
    return sonuc

@zaman_hesapla
def tola(*args):
    time.sleep(1)
    return(sum(args))
 
print(kareleri_al(range(10)))           # ��lem 0.0 saniye s�rd�.
                                        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(kupleri_al(range(10)))            #��lem 0.0 saniye s�rd�.
                                        # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# çok fazla fonksiyona sahip bir projede çalıştığında, hepsi için aynı işlemleri yapmak istemiyorsan, zaman hesapla decoratoru ile hepsi için aynı işlemi yapabilirsiniz.

# şöyle bir kuullanım da olabilir: diyelim ki siz hava durumunu kontrol eden veya borsayı kontrol eden bir uygulama yazdınız, yani web'ten sürekli request atıp gelicek olan sonuçları işliyo  olabilirsiniz. siz programınızı çalıştırdığınızda diyelim ki saniyede 1 milyon tana request atmak istemiyorsun.
# sen bir decorator oluşturursun, o iki request arasında 10 saniye zaman koyar.
# umarım decoretoru anlamışsınızdır. bundan sonraki dersimizde OOP'deki decorator kullanımına değineceğiz.
