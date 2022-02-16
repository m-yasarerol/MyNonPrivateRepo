# Inheritance - kalıtım 2
# Kalıtım, miras alma, anne ve babanın çocuğa özellik aktarımı
# bir Clasımız olacak, biz o clastan alt claslar üreteceğiz ancak oluşturduğumuz yeni alt claslar bazı özelliklerini miras olarak alacaklar.

class calisan:      # kalıtım almadığı için parantez açmadım
    zam_orani = 1.1
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_göster(self):
        return "Ad: {} Soyad: {} Maas:{} Email:{}".format(self.isim,self.soyisim,self.maas,self.email)

calisan1 = calisan("Ali","Çalışkan", 5000)
calisan2 = calisan("Veli","Uzun", 6000)

#şimdi bu class'tan miras alan başka bir class oluşturalım
class Yazilimci(calisan):
    zam_orani = 1.2   
    def __init__(self, isim, soyisim, maas,bildiği_dil):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
        self.bildiği_dil = bildiği_dil    
    def bilgileri_göster(self):
        return "Ad: {} Soyad: {} Maas:{} Email:{} Bildiği dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildiği_dil)
    def dilini_soyle(self):
        return f"Bildiğim dil: {self.bildiği_dil}"

yazilimci1 = Yazilimci("Ayşe","Yıldız",7000,"Phyton")    
yazilimci2 = Yazilimci("Fatma","Ay",8000,"Phyton")
print(yazilimci1.email)                 #Ay�eY�ld�z@sirket.com
print(yazilimci2.bildiği_dil)           #Phyton
#yazılımcı clasının içine hiçbir şey almasam da calisan clasının özelliklerini aldı
#yeni oluşturduğumuz claslar eski özellikleri mutlaka taşımalı, ancak bunlardan bazıları biraz değişik olabilir
print(calisan2.zam_orani)   #1.1
print(yazilimci1.zam_orani) #1.2        # class içinde belirtmeseydim, miras aldığı clasın zam oranını alırdı
# yeni bir yazılımcı tanımladığımda, yazilimci clasının init fonk. yok ise, kalıtım adlığı clasın init fonksiyonunu kullanır. Varsa zaten kendi init fonkisonunu kullanır
print(calisan2.bilgileri_göster())      # Ad: Veli Soyad: Uzun Maas:6000 Email:VeliUzun@sirket.com
print(yazilimci1.bilgileri_göster())    # Ad: Ay�e Soyad: Y�ld�z Maas:7000 Email:Ay�eY�ld�z@sirket.com Bildi�i dil: Phyton
# yazılımcı clasında bilgileri_göster diye bir fonk. oluşturmasaydım, yazlımcı clasında bilgileri_göster diye bir şey olmadğndan miras aldığı sınıfa gidip çalıştırırdı.
# Dolayısıyla yukarıdaki iki kodun çıktısı aynı olurdu
# ben eğer yazlımcya extra bir özellik eklemek istiyorsam onun init fonk. baştan tanımlamam gerekiyor ve oraya da bildiği dil değişkenini eklemem gerkiyor.
# önceki aynı değişkenleri yazmama gerek yoktu. super fonksiyonunu kullanabilirdik. mesela müdür sınıfında uygulamalı görelim:

class mudur(calisan):
    def __init__(self, isim, soyisim, maas,kavramsal_beceri):
        super().__init__(isim, soyisim, maas)   # gördüğün gibi kalıtım adlığım fonk. değişkenleri toplu olarak tanımladım
        self.kavramsal_beceri = kavramsal_beceri
mudur1 = mudur("Yaşar","Erol",8000,"Analitik düşünme")

print(mudur1.kavramsal_beceri)
