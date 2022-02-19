# OOP @property, @setter, @deleter,decorator kullanımı
# bunlar phyton'da gömülü halde yani hazır bulunan class'lardır
# bu dersimizden sonra OOP'ye küçük bir nokta koyacağız.
# ne işe yarıyor?
from tkinter import N


class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        self.adsoyad = ad + " " + soyad
    
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"

kisi1 = Kisi("Ahmet","Uzun")
kisi1.ad = "Ali"
print(kisi1.ad)             #Ali
print(kisi1.adsoyad)        #Ahmet Uzun
print(kisi1.email())        #Ali.Uzun@sirket.com
#email'de parantez var: neden? ad ve soyad bir özellikti, e mail ise bir metottur. yani clas'a ait bir fonksiyondur. ancak onu çalıştırdığımız zaman bize değer döndürür.
# neden veri tutarszlığı oluştu.?
# email metodu hep en güncel versiyonu kullandı, ancak ad soyatta böyle olmadı. çünkü hafızada ad, soyad, ve adsoyad başka yerlerde. adı sonradan değiştirmemiz bir şeyi etkilemez.

# bu problemi çözmeye çalışalım:
class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    def adsoyad(self):                      # bu artık bizim için bir özellik değil bir metot. dolayısı ile buradan bize bilgi gelmesi için bunu çalıştırmamız lazım. yani sonuna "()" koyacağız
        return f"{self.ad} {self.soyad}"

    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"

kisi1 = Kisi("Ahmet","Uzun")
kisi1.ad = "Ali"
print(kisi1.ad)                             #Ali
print(kisi1.adsoyad())                      #Ali Uzun
print(kisi1.email())                        #Ali.Uzun@sirket.
# ancak burada şöyle bir sorun oluştu. Siz böyle bir değişiklik yaptığınızda, sizin bu class'ınızı kullanan diğer bütün claslar bu özelliği değiştirmeli, yani önceden adsoyad bir özellikti, artık bir metot
# dolayısı ile bu büyük ölçekli programlarda çok büyük bir problem. çünkü hangi clasların birbiri ile etkileşimde olduğunu teker teker tespit etmeniz gerekiyor. o nedenle bu kullanım çok doğru değil.
# bu yüzden property decorator'unden faydalanıyoruz.
class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property       # property decoratun yaptığı şey sizin methodlarınıza bir özellik gibi yaklaşmanızı sağlar. siz bunu bu şekilde değiştirdiğiniz zaman yine ad soyadı çağırırken parantez olmadan  çağırabileceksiniz. sadece bu kısmı değiştirdik. yani property decoratoru sizin içeride oluşturduğunuz metotlara sanki biz alan özelliğiymiş gibi kullanabilmenizi sağlar.
    def adsoyad(self):                      
        return f"{self.ad} {self.soyad}"
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"

kisi2 = Kisi("Ayten","Can")
kisi2.ad = "Cansu"
print(kisi2.ad)                          
print(kisi2.adsoyad)                # gördüğün gibi ilk seferki şekilde kullandım. artık bir özellik olmadığı halde.      
print(kisi2.email)                        
# ad soyadı bir fonk. olarak tanımladık, ama bir alanmış/ özellikmiş gibi erişmemizi sağladı.

kisi2.adsoyad = "Cansu Cansız"          
#>> error: özelliği ayarlayamıyorum. çünkü aslında öyle bir özellik yok. o bir metot. şimdi bunu halletmeye çalışalım
# bunu yapmak içinde setter decoratorunden faydalanacağız.
class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property        # property decoratun yaptığı şey sizin methodlarınıza bir özellik gibi yaklaşmanızı sağlar. siz bunu bu şekilde değiştirdiğiniz zaman yine ad soyadı çağırırken parantez olmadan  çağırabileceksiniz. sadece bu kısmı değiştirdik. yani property decoratoru sizin içeride oluşturduğunuz metotlara sanki biz alan özelliğiymiş gibi kullanabilmenizi sağlar.
    def adsoyad(self):                      
        return f"{self.ad} {self.soyad}"
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"

    @adsoyad.setter  # setter ise yukarıdaki gibi bir atama yaptığınızda, yani bir şeyi set etmek istediğinizde otomatik olarak bu fonk. çalışacak
    def adsoyad(self,isim):
        ad,soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad

kisi3 = Kisi("Burak","Gülnur")
kisi3.ad = "Burakcan"
kisi3.adsoyad = "Burak Can"

print(kisi3.ad)
print(kisi3.adsoyad)
print(kisi3.email)
# yani bu da property'i kullandığımız hemen hemen her zaman kullandığımız bir decorator. çünkü normalde burada adsoyad isimli bir özellik yok. bu bir metot.
# buna atama yapmak istediğimiz zaman yani bir şeyi set etmek istediğimizde otometik olarak setter decoratoru çalışacak

# bir de bir şeyi silmek istersek eğer:
del kisi3.ad        # program hata verir. çünkü ad diye bir değişken yok artık.
# mesela ben bir ad soyad girdim. ama yanlış girmişim. silmek istiyorum diyelim ki
# deleter kullanacağız.
class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property        # property decoratun yaptığı şey sizin methodlarınıza bir özellik gibi yaklaşmanızı sağlar. siz bunu bu şekilde değiştirdiğiniz zaman yine ad soyadı çağırırken parantez olmadan  çağırabileceksiniz. sadece bu kısmı değiştirdik. yani property decoratoru sizin içeride oluşturduğunuz metotlara sanki biz alan özelliğiymiş gibi kullanabilmenizi sağlar.
    def adsoyad(self):                      
        return f"{self.ad} {self.soyad}"
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"

    @adsoyad.setter  # setter ise yukarıdaki gibi bir atama yaptığınızda, yani bir şeyi set etmek istediğinizde otomatik olarak bu fonk. çalışacak
    def adsoyad(self,isim):
        ad,soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad

    @adsoyad.deleter    # nasıl ki setter, bir atama yaptığımızda otomatik olarak çalışıyordu, bu da "del" dediğinizde çalışacak
    def adsoyad(self):
        print("silindi")
        self.ad = None
        self.soyad = None

kisi4 = Kisi("Ceylan","Kaya")
del kisi4.adsoyad               #silindi
print(kisi4.ad)                 #None
print(kisi4.adsoyad)            #None None
print(kisi4.email)              #None.None@sirket.com
#kişi hala mevcut. sadece ad ve soyad bilgisini sildim. email adresini oluşturduğunu görüyoruz.

# bakın phytona 3 adet "adsoyad" tanımladık, bizim yapmak istediğimiz işleme göre hangisini kullanacağına kendisi karar veriyor. 
# >> erişmek istediğimizde property'ye gidiyor.
# >> set etmek istediğimizde setter'in altındaki fonksiyonu kullanıyor
# >> del dediğimizde deteler'i kullanıyor. 
# yani bunların içerisine ihtiyacınıza göre kod yazabilirsiniz.
