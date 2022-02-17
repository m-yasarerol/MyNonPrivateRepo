# magic methodlar incelemeye devam ediyoruz
# neydi bunlar, phytonda bulunan özel gömülü methodlardı, yaptıkları iş bir class tanımladığınızda onun üzerinde yapabileceğiniz işlemleri belirleyebildiğiniz methodlardı
# __str__ ve __repr__
# bunların yaptığı iş ise oluşturduğunuz class'tan ürettiğiniz bir nesnenin nasıl stringe dönüştürüleceği, yani yazdır dediğinizde ekrana nasıl yazılacağını belirleyen iki fonk.

# ikisinin birbirinden farkını inceleyelim
a= "Phyton"
print(str(a))           #Phyton: sadece metnin kendisini yazdırdı
print(repr(a))          #'Phyton': tırnaklarını da yazdırdı

b = 2 / 11
print(str(b))           #0.18181818181818182
print(repr(b))          #0.18181818181818182>> fark göremedim

from datetime import date
bugun = date.today()
print(bugun)            #2022-02-17
print(str(bugun))       #2022-02-17
print(repr(bugun))      #datetime.date(2022, 2, 17)>>datetime objesi olduğunu ver parametrelerini de gösterdi

# str fonk. kullanıcın görmesini istediğimiz veriyi döndürür. son kullanıcı parametreler ile ilgilenmez
# repr geliştiricinin kendisi için faydalıdır. debug arayan bir yazılımcı kullanabilir. kullanıcıya gösterilmez

# peki biz bunları nasıl kullanacağız?
# bir şeyi print ettiğinizde fonk. ince str ye, bulamazsa repr ye bakyor.
class futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

futbolcu1 = futbolcu("Ali","Veli",20)
print(futbolcu1)             #<__main__.futbolcu object at 0x00000006F200FFD0>: istediğimiz gibi yazdırmadı, clasta str diye bir şey bulamadığı için böyle yazdı

# bunu istediğim gibi yazdırmak istiyorsam:
class futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    def __str__(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} Yaş: {self.yas}"
    def __repr__(self):
        return f'Futbolcu("{self.isim}","{self.soyisim}","{self.yas}")'
futbolcu2 = futbolcu("Mustafa","Topal",30)
print(futbolcu2)            #Ad: Mustafa Soyad: Topal Ya�: 30
                            #hem str hem repr bulunduğu için str yi tercih etti.
#özellikle repr ile yazdırmak istiyorsam:
print(repr(futbolcu2))      #Futbolcu("Mustafa","Topal","30")
print(futbolcu2.__repr__()) #Futbolcu("Mustafa","Topal","30")

# str ve repr nin ikisi de string, yazdırılebilir ifadeler üretir, str son kullanıcı içindir, repr ise yazdırılsın ama clası, parametreleri ile ilgili bilgiler de bulundurur.
# repr'yi doğru şekilde tanımlayabilmek için, print çıktısını alıp bir değişken olarak yeniden tanımlamak istediğinizde hata vermeyecek şekilde yazmanı gerekiyor.
