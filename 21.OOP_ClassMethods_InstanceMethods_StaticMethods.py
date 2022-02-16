# artık nesne yönelimli programlamanın içerisindeyiz
# ilk dersimizde class kavramını öğrendik
# sonrasında nesne ve sınıf değişkenlerine bakmıştık
# bu dersimizde size nesnelere ce sınıflara özgü metotlardan bahsedeceğim

# minik bir tekrar
class kisi:                             # isim ve yaş, clasın kendisine ait değişkenler değil
    zam_orani = 1.1                     # class variable
    kisi_sayiyi = 0
    def __init__(self,isim,yas):        # bunların ismi instance variables, yani nesnelere ait olan değişkenler, sınıfın yaş isimli bir değişkeni yok, sınıftan üreteceğimiz kişilerin var
        self.isim = isim                # self: clastan bir nesne ürettiğimde oluşturduğum değişkenin yerine geçiyor
        self.yas = yas                  # instance variable
        kisi.kisi_sayiyi += 1
kisi1 = kisi("Ali",20)
kisi2 = kisi("Vei",30)

# gelelim bunların metotlarına
class kisi:                             
    zam_orani = 1.1                     
    kisi_sayiyi = 0
    def __init__(self,isim,yas):        
        self.isim = isim                
        self.yas = yas                  
        kisi.kisi_sayiyi += 1
    def bilgilerini_soyle(self):        # instance method
        return(f"Ad: {self.isim} Yas: {self.yas}")

kisi1 = kisi("Ali",20)
kisi2 = kisi("Vei",30)
print(kisi1.bilgilerini_soyle())        #Ad: Ali Yas: 20
# class'ın içerisinde hiçbir şey yazmadan direkt def yazarak oluşturduğum bir method instance methoddur. Çünkü içerisine otomatik olarak self parametresini aldı.
# bu, bizim oluşturduğumuz bir instance'ile beraber kullanılacağı anlamına gelir. instance selfin yerine geçer ve fonksiyon çalışır
# sadece clas ile beraber kullanırsam hata alırım
print(kisi.bilgilerini_soyle())         # error! : self yok

# class method:
# clas method, nesne ile değil de class'ın kendisi ile alakalı olan bir methoddur. bunu herhangi bir kişi oluşturmadan da kullanabilirsiniz.
# class method nasıl tanımlanır? "@classmethod" ile.
class kisi:                             
    zam_orani = 1.1                     
    kisi_sayisi = 0
    def __init__(self,isim,yas):        
        self.isim = isim                
        self.yas = yas                  
        kisi.kisi_sayiyi += 1
    def bilgilerini_soyle(self):        
        return(f"Ad: {self.isim} Yas: {self.yas}")
    @classmethod 
    def kisi_sayisini_soyle(cls):       # cls'yi otomatik olarak alması gerek, ama bende almadı
        return cls.kisi_sayisi          # cls, bizim fonk. çağırırken kullandığımız clas
print(kisi.kisi_sayisini_soyle())       # 0

# burdan nesne üretmeden herhangi bir fonk. alıştırabilmek ne işimize yarar?
# bunu bir constructor olarak kullanmak, diyelim ki sisteme toplu üye kaydı yapacaksın, bir yerden 10.0000 üye alıcaksın ama  isim ve soy ismin yanına "-" koymuşlar. Yani farklı bir formatta, her üye eklemek için elle yazmak yerine, bir tane fonk. yazıcaz bunu otomatik olarak bizim istediğimiz formata çevirip bizim için kişi clasınan nesne üretecek
# yani bize bir yerden 10.000 adet üye geldi ama bilgiler "ayse-25" formatında tutulmuş, elle yazmak yerine dosyayı okuyacaz, stringi bölücez, istediğimiz formata getirip yeni nesne oluşturacağız
# karışık oldu farkındayım, örnek üzerinde görelim 
class kisi:                             
    zam_orani = 1.1                     
    kisi_sayisi = 0
    def __init__(self,isim,yas):        
        self.isim = isim                
        self.yas = yas                  
        kisi.kisi_sayisi += 1
    def bilgilerini_soyle(self):        
        return(f"Ad: {self.isim} Yas: {self.yas}")

    @classmethod 
    def kisi_sayisini_soyle(cls):      
        return cls.kisi_sayisi   

    @classmethod      
    def string_ile_olustur(cls,str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)            # böylece class'tan bir tane daha nesne oluşturup onu geri döndüreceğiz.

kisi1 = kisi("Ali",20)
kisi2 = kisi("Veli", 30)
kisi3 = kisi.string_ile_olustur("Ayse-25")
print(kisi.kisi_sayisini_soyle())       # 3
print(kisi3.isim)                       # ayse

# bir tane daha yapalım, diyelim ki sizin için veri toplayan birileri yanlış yapmış, yaşlarını istemek yerine doğum yılını almış, bir teker teker hesaplamak yerine fonksiyonla yapabiliriz.
from datetime import date
class kisi:    # date'yi import ettim, bu sayede bulunduğumuz tarihten doğum tarihini çıkartarak kişinin yaşını bulacağız                     
    zam_orani = 1.1                     
    kisi_sayisi = 0
    def __init__(self,isim,yas):        
        self.isim = isim                
        self.yas = yas                  
        kisi.kisi_sayisi += 1
    def bilgilerini_soyle(self):        
        return(f"Ad: {self.isim} Yas: {self.yas}")

    @classmethod 
    def kisi_sayisini_soyle(cls):      
        return cls.kisi_sayisi   

    @classmethod      
    def string_ile_olustur(cls,str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)

    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili):
        return cls(isim,date.today().year - dogum_yili)     # bu günün yılından doğum yılını çıkaracağım

kisi1 = kisi("Ali",20)
kisi2 = kisi("Veli", 30)
kisi3 = kisi.dogum_yili_ile_olustur("Elif",1990)
print(kisi3.isim,kisi3.yas)         # Elif 32
print(kisi.kisi_sayisini_soyle())   # 3

# instance methodun anlam kazanması için bir nesne üretmeliyim. 
# herhangi bir instanceye bağlı olmayan fonk. sınıfın kendisine ait olan fonkisyon denir. farklı şekillerde eleman üretebilmenin önünü açar


# statik metot: otomatik olarak parametre almaz, 
from datetime import date
class kisi:                             
    zam_orani = 1.1                     
    kisi_sayisi = 0
    def __init__(self,isim,yas):        
        self.isim = isim                
        self.yas = yas                  
        kisi.kisi_sayisi += 1
    def bilgilerini_soyle(self):        
        return(f"Ad: {self.isim} Yas: {self.yas}")

    @classmethod 
    def kisi_sayisini_soyle(cls):      
        return cls.kisi_sayisi   

    @classmethod      
    def string_ile_olustur(cls,str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)          
    
    @staticmethod 
    def dogum_yili_hesapla(kisi):               # içine otomatik olark değişken almaz
        return date.today().year - kisi.yas
kisi1 = kisi("Yasar", 20)            
print(kisi.dogum_yili_hesapla(kisi1))           # 2002

# fark: class method clasa bağlı
# statik metot, parametreyi otomatik olarak bağlar, clasa bağlı değil.
# bir sonraki dersimiz kalıtım. 
