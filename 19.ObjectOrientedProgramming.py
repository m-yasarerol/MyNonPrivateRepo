# Nesne yönelimli programlamaya küçük bir giriş yapacağız

# Class kavramıyla başlayalım, nedir ne işe yarar? 
# Class nesne yönelimli programlamanın en önemli kavramlarından birisidir .çünkü her şey claslar ile alakalı
# class sınıf demektir, birbiri ile ortak özellikli olan nesneleri bir şekilde gruplayıp, daha düzenli bir programa sahip olmak amacı ile yapılır

# Örnek: bir alışveriş sitesinin otomasyonunda çalışıyorsun, orada bir sürü değişken var, 10 binlerce müşeri, ürün ve çalışan var. neyin ne olduğu belli olsun diye bunları sınıflandıracaksınız
# mesela:
# Sınıf (class)           Snıf (class)            Snıf (class)
# Müşteri                 Ürün                    Personel
# -------                ------                   --------
# Adı                     Adı                     Adı
# soyadı                  Stok kodu               Soyadı
# yaş                     Stok adedi              Maaş
# email                   Fiyat                   Departmanı
# id
    
# instance(id)            Instance(ornek)         Instance(ornek)
# Ali,Veli,20,            klavye                  Ahmet
# ali@veli.com            ABC123                  Mehmet
# 17                      71                      5.000
# fonk: satın al          39.90                   lojistik
#                                                 fonk:ürün ekle

# müşteri snıfı demek, müşteri sınıfı cinsinden bir değişken oluşturacağın zaman, kullanacağın taslak demek
# bunu bir kağıda yazılmış olan form olarak düşünebilirsin

# aynı şekilde bir ürün kayıt edecekseniz ürün şablonunu kullanacaksınız

# yani nesne yönelimli programlama, günlük hayatta karşılaştığımız problemler ile programlamadaki mantığı birbirine yaklaştırmak üzerine düşünülmüş bir kavram

# class, ortak özellikleri olan nesneleri grupladığımız bir yapıyı ifade eder.
# Instance, clastan ürettiğimiz bir örnek, ya da meşhur ismi ile nesnemiz.
# yukarıdaki şablon class, alttaki ise clastan ürettiğimiz nesne(ınstance)

# bir class nasl oluşturulur? class anahtar kelimesi phyton'a bir sınıf oluşturacağımızı söyler
class calisan:
    pass                # içine herhangi bir şey yazmadım, sonradan doldurucam

calisan1 = calisan()    # artık elimde calisan isimli bir clasım, calisan1 isminde ise o clastan üretilmiş bir örneğim var

calisan1.name = "Ali"
calisan1.surname = "Veli"
calisan1.yas = 20
print(calisan1.name)    # Ali     
print(calisan1.surname) # Veli

calisan2 = calisan()
calisan2.email = "a@b.com"
print(calisan2.email)   #a@b.com

# yukarıdaki kullanım yanlıştır, ortak özelllikleri sınıflamadık. şu şekilde yapmalıyız.
class calisan:
    def __init__(self,name,surname,age):     
        print("__init__ fonksiyonu çalışıyor")       
        self.name = name
        self.surname = surname
        self.age = age

calisan1 = calisan("Ali", "Veli", 20)               # __init__ fonksiyonu çalışıyor
print(calisan1.name,calisan1.surname,calisan1.age)  #Ali Veli 20
# ben burda çalışan sınıfına bir veri gönderdiğimde ilk önce __init__ fonksiyonu çalıştı ve li nameya,veli surnameye, 20 yaşa geldi
#self benim oluşturduğumu değişkendir, onu varsayılan olarak kendisi gönderiyor zaten, ayrıca self yazmadım
#yukarıdaki örnekte gösterdiğim gibi oluyor
# bu kısmını anladıysanız olayın çok büyük bir kısmını hallettiniz demektir
calisan2 = calisan("Ahmet", "Mehmet", 25)
print(calisan2.name,calisan2.surname,calisan2.age)  # __init__ fonksiyonu �al���yor
                                                    # Ahmet Mehmet 25

# peki ya biz sınıfımıza bir metot eklemek isterse? yani bir fonksiyon yazacağız, bir clasa bağlı fonkisyonlara metot denir, görelim
class calisan:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):        # calisan 2 dediğinde o çalışan fonksiyona self olarak gitti, hangi fonk. üzerinden o fonkisyonu çağırdıysan self o değişken oluyor
        print(f"Adı: {self.name}  Soyadı: {self.surname}  Yaş: {self.age}")
calisan1 = calisan("Ali","Veli",20)
calisan2 = calisan("Ahmet","Mehmet",25)
calisan1.show_info()            #Ad�: Ali  Soyad�: Veli  Ya�: 20
calisan2.show_info()            #Ad�: Ahmet  Soyad�: Mehmet  Ya�: 25

calisan.show_info()             #error!: self eksik, calısan 1 ve 2 nesne idi, fonksiyonu onlar üzerinden çağırdığımda selfe hemen onları atadı. Sınıfın kendisi üzerinden çağırdığımda ne göndereceğini bilemedi, ama bunun içine o örenklerden birini yazarsam sorun çıkmaz
calisan.show_info(calisan1)     #sorun olmaz

# class nedir ne işe yarar birazcık anladık. class ortak özelliği olan elemanları gruplamak için kullandığımız bir yapı
# classlara ait fonkisyonlara metot deniyor unutma

# >>KULLANICI CLASA EKSİK VERİ GİRERSE?<<
# diyelim ki siz bir form oluşturdunuz, bazı kısımları boş bırakıyorsun, bazı kısımlar zorunlu oluyor. mesela age kısmını boş biraktığımızda age=0 olarak tanımlaman gerekir, görelim
class calisan:
    def __init__(self,name="girilmedi",surname="girilmedi",age=0):
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):        # calisan 2 dediğinde o çalışan fonksiyona self olarak gitti, hangi fonk. üzerinden o fonkisyonu çağırdıysan self o değişken oluyor
        print(f"Adı: {self.name}  Soyadı: {self.surname}  Yaş: {self.age}")
calisan1 = calisan("Ali")
calisan1.show_info()            #Ad�: Ali  Soyad�: girilmedi  Ya�: 0
# adını ve soy adını girip yaşını girmek istiyorsan
calisan2 = calisan("Mehmet", 20)
calisan2.show_info()            #Ad�: Mehmet  Soyad�: 20  Ya�: 0
# olmadı, soyadını 20 tanımladı. çünkü bunlar sırayla gidiyor.
# o yüzüden böyle bir durumda surname'yi boş bırakmak istiyorsan şu şekilde yapacaksın.
calisan3 = calisan("Mahmut", age=20)
calisan3.show_info()            #Ad�: Mahmut  Soyad�: girilmedi  Ya�: 20
# sadece yaş girmek isteseydim:
calisan4 = calisan(age=20)
calisan4.show_info()            #Ad�: girilmedi  Soyad�: girilmedi  Ya�: 20

# init fonkisyonu çok önemli, clastan bir nesne oluşturduğumuzda otomatik olarak çalışır
# self çok önemli selfi anlamadan çok fazla ileri gidemeyiz.
