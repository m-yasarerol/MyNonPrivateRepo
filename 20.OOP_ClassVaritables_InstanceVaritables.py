# class caritables - instance varitables
# sınıf değişkenleri ve nesnelerin değişkenleri
# örnek class:
class calisan:
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas
calisan1 = calisan("Ali", 5000)
calisan2 = calisan("Ahmet", 6000)
# bu bizim geçen ders yaptığımı şeydi
print(calisan1.__dict__ )       # {'isim': 'Ali', 'maas': 5000}
print(calisan2.__dict__)        #{'isim': 'Ahmet', 'maas': 6000}
# çalışanların sahip oldukları özellikleri bir sözlük olark karşıma getirdi.

# calısan1 ve calısan2 instance variabledir, yani nesnelerin değişkenleri
# peki ben bu sınıftaki herkes için ortak olan bir değişken tanımlamak istersem?
# bunu neden yapan yapayım? mesela bu çalışanları çalıştıran firmanın bir zam politikası var ve herkese aynı zammı yapıyor:
class calisan:
    zam_orani = 1.1
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas
calisan1 = calisan("Ali", 5000)
calisan2 = calisan("Ahmet", 6000)
# peki bu zam oranına nasıl erişebilirim?
print(calisan.zam_orani)        # 1.1: class'ın kendi üzerinden eriştim 
print(calisan1.zam_orani)       # 1.1: class'tan ürettiğim bir nesne üzerinden de erişebiliyorum
print(calisan2.zam_orani)       # 1.1
print(calisan.__dict__)         # özelliklerde zam oranı var
print(calisan1.__dict__)        # özelliklerde zam oranı yok
#neden? 
# siz zam oranı değişkenine erişmek istediğinizde ilk önce değişkenin kendisine bakıyor, sonrasında class'a bakıyor
calisan.zam_orani = 1.2         
print(calisan.zam_orani)        # 1.2
print(calisan1.zam_orani)       # 1.2
print(calisan2.zam_orani)       # 1.2
# hem clasa hem de değişkenlerin hepsine etki etti.
# ancak şöyle yaparsam
calisan1.zam_orani = 1.3
print(calisan.zam_orani)        # 1.2
print(calisan1.zam_orani)       # 1.3
print(calisan2.zam_orani)       # 1.2
# class'n kendi ismi üzerinden erişip değiştirirsen tüm nesneleri için değişir
# ama belirli bir nesne üzerinden erişip zam oranını değiştirirsen sadece o değişken için değişir

print(calisan1.__dict__)        # {'isim': 'Ali', 'maas': 5000, 'zam_orani': 1.3}
print(calisan2.__dict__)        # {'isim': 'Ahmet', 'maas': 6000}
# eğer siz bunu class üzerinden erişirsen hepsine etki eder,nesne üzerinden erişirsen yukarıda gördüğün gibi o değişken için sadece o esneye etki eder, orada yeni bir özellik oluşur.

# zam oranı yerine personel saysı olsun, her personel eklendiğinde bu 1 artsın
class calisan:
    personel_sayisi = 0
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas
        calisan.personel_sayisi += 1    # self değil çalışan yaptım, eğer self yapsaydım sınıfa değil de değişkene ait olurdu, anlamsız olurdu.
print(calisan.personel_sayisi)      # 0
calisan1 = calisan("Veyse", 5000)   
print(calisan.personel_sayisi)      # 1
calisan2 = calisan("Osman", 5000)
print(calisan.personel_sayisi)      # 2
calisan3 = calisan("Yaşar", 5000)
print(calisan.personel_sayisi)      # 3
# her çalışan eklendiğinde fonksiyon yeniden çalışır. 
