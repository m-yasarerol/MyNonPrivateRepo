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

# önceki aynı değişkenleri yazmama gerek yoktu. super fonksiyonunu kullanabilirdik. mesela yönetici sınıfında uygulamalı görelim:

# KALITIM DERS 2
# şimdi bir de yönetici sınıfı oluşturacağız, o da çalışandan türeceyek, ancak yönetici snıfında da diğerlerinde olmayan başka bir özellik olacak
# sorumlu oldupu çalışanlar olacak, ve bu yöneticiye çalışan ekleyip silecebileceğiz, kimlerden sorumlu olduğunu listelicez
class Yonetici(calisan):
    def __init__(self, isim, soyisim, maas, calisanlar = None):     # önce yöneticiyi oluşturup sonra kimlerden sorumlu olduğunu belirleyeceğim. o nedenle "none" yazdım
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
        
    def calisan_ekle(self,calisan):                             # calisan ekleme fonk.
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)                     # eğer çalışan bu listede yoksa ekle

    def calisan_sil(self,calisan):                              # calisan silme fonk.
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)                     # eğer çalışan bu listede varsa sil

    def calisanlari_goster(self):                               # sadece self yazdı çünkü görüntülemek istediğim çalışanları ben girmeyeceğim
        for calisan in self.calisanlar:
            print(calisan.bilgileri_göster())

yonetici1 = Yonetici("Metin","Ali",10000)
yonetici1.calisan_ekle(calisan1)
yonetici1.calisan_ekle(yazilimci1)
yonetici1.calisanlari_goster()                                  #Ad: Ali Soyad: �al��kan Maas:5000 Email:Ali�al��kan@sirket.com
                                                                #Ad: Ay�e Soyad: Y�ld�z Maas:7000 Email:Ay�eY�ld�z@sirket.com Bildi�i dil: Phyton
yonetici1.calisan_sil(calisan1)
yonetici1.calisanlari_goster()                                  #Ad: Ay�e Soyad: Y�ld�z Maas:7000 Email:Ay�eY�ld�z@sirket.com Bildi�i dil: Phyton
# yöneticimizin ekleme,silme ve görüntüleme fonk. hepsi düzgün bir şekilde çalışıyor

# bir de çalışanları elle girelim
yonetici2 = Yonetici("Feyyaz","Beşiktaş",11000,[yazilimci1,yazilimci2,calisan1])
yonetici2.calisanlari_goster()                                  #Ad: Ay�e Soyad: Y�ld�z Maas:7000 Email:Ay�eY�ld�z@sirket.com Bildi�i dil: Phyton
                                                                #Ad: Fatma Soyad: Ay Maas:8000 Email:FatmaAy@sirket.com Bildi�i dil: Phyton
                                                                #Ad: Ali Soyad: �al��kan Maas:5000 Email:Ali�al��kan@sirket.com

# bir sınıf, başka bir sınıfın alt clas' mı veya ondan üretilmiş bir nesne mi nasıl kontrol edeceğiz?
print(isinstance(yonetici2,calisan))        # True: yani yonetici 2 bir calisandir, yani calisandan üretilmiş bir instance'dir(örnektir)
print(isinstance(yazilimci1,Yonetici))      # False
# yani bu isinstance demek, birinci yazdığınız nesne, ikinci yazdığınızdan üretilmiş mi? o anlama geliyor.

#issubclas: bir clas başka bir clasın alt clası mı? ondan türetilmiş mi
print(issubclass(calisan,Yazilimci))        # false: bu soru şu anlama gelir: çalışan, yazılımcıdan türedi mi?
print(issubclass(Yazilimci,calisan))        # True: yazılımcı, çalışan clasından türemiş bir clas mıdır?

# bu sorular ile bir class başka bir clasın alt clası mı?
# bir nesne verdiğimiz bir clastan türemiş mi mi türememiş mi? .. kontrol edebiliyoruz.
