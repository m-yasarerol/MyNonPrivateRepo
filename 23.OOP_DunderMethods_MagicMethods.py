# Nesne yönelimli programlamanın önemli başlıklarından devam ediyoruz.
#dunder ve magic methods, biraz ileri düzey fonksiyonlar
# bunlar nedir ve ne işe yarıyorlar
print(3 + 5)                            # topladı
print(int.__add__(3,5))                 # arka planda gerçekleşen ifade

print("Ali" + "Veli")                   # uc uca ekledi
print(str.__add__("Ali","Veli"))        # arka planda gerçekleşen ifade

print([1,2,3] + [4,5,6])                # tek bir listede elemanları birleştirdi
print(list.__add__([1,2,3],[4,5,6]))

# 3 adet "+" var ama her birinin işlevi farklı. Yani "add" methodu her sınıf için ayrı ayrı tanımlanmış
# yani biz de kendimize ait bir clas oluşturursak ve o clastan ürettiğimiz nesnelerin mesela toplama öz. sahip olmalarnı istiyorsan bu "ad" methodounu istediğimiz şekilde tanımlamamız gerekiyor
# kendimize bir clas oluşturalım
class Mylist(list):
    def __add__(self, other):
        if len(self) != len(other):     # listelerin eleman sayısı eşit değilse toplanamasın
            return "Bu elemanlar toplanamaz" 
        else:
            result = Mylist()
            for i in range(len(self)):
                result.append(self[i] + other[i])   
        return result
    
    def __sub__(self, other):           #2
        if len(self) != len(other):     # listelerin eleman sayısı eşit değilse çıkartmasın
            return "Bu elemanlar çıkarılamaz" 
        else:
            result = Mylist()
            for i in range(len(self)):
                result.append(self[i] - other[i])   
        return result

    def __eq__(self, other):            #3
        if sum(self) == sum(other):
            return True
        return False

    def __abs__(self):                  # 4 - mutlak değer fonk.
        result = Mylist()
        for i in self:
            if i >= 0:
                result.append(i)        # direkt ekledim
            else:
                result.append(-1 * i)   # 0'dan küçükse -1 ile çarpıp ekledim
        return result

liste1 = Mylist([1,2,3])
liste2 = Mylist([4,5,6])
print(liste1 + liste2)                  #[5, 7, 9]
# 2: dolayısıyla kendi ihtiyacıma göre bir toplama işlemini kendi ihtiyacıma göre tanımladım
# bir de çıkartma işlemi tanımlayalım
print(liste1 - liste2)                  #[-3, -3, -3]

# 3: listenin uzunluğu ile ilgili bir fonk. tanımlayalım, kümelerin toplamı birbirine eşit ise iki küme birbirine eşit olsun
# diyelim ki o kümelerdeki sayılar gol sayılarını ifade ediyor.
print(liste1 == liste2)                 # False, çünkü toplamları birbirine eşit değil
# normalde bu listeler birbirine eşit değil tabi ki, ama benim aradığım eşitlik koşulunu karşılıyor, eşitliği yeniden tanımladım

# 4 : benim burada istediğim şey, negatifleri pozitif yapsın
liste3 = Mylist([-1,2,-9])
print(abs(liste3))                      #[1, 2, 9]

# yani kendiniz bic class oluşturacaksınız, clasın kurallarını kendi ihtiyacınıza göre şekillendirebilirsiniz. bunu yaparken kullanacağınız methotlar;
#"__" ile başlayan dunder methodları olacak

# yeni bir sınıf oluşturup kendimiz özellik ekleyelim
class Futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def __eq__(self,other):             # 2 futbolcunun isim ve soy isimleri eşit ise bu futbolcular aynı olsun
        if self.isim == other.isim and self.soyisim == other.soyisim:
            return True
        return False

    def __add__(self,other):            # yeni bir toplama fonk. tanımlayalım, isim ve soy isimlerin ilk elemanlarını toplasın
        isim = self.isim[0] + other.isim[0]
        soyisim = self.soyisim[0] + other.soyisim[0]
        yas = self.yas + other.yas
        return Futbolcu(isim,soyisim,yas)

    def __lt__(self,other):             # iki futbolcunun yaşlarını baz alarak büyüklük- küçüklük tanımlayalım
        if self.yas < other.yas:
            return True
        return False
    
    def __gt__(self,other):
        if self.yas > other.yas:
            return True
        return False

futbolcu1 = Futbolcu("Ali","Veli",27)
futbolcu2 = Futbolcu("Ali","Ahmet",30)
print(futbolcu1 == futbolcu2)           # False

futbolcu3 = futbolcu1 + futbolcu2
print(futbolcu3)                        #<__main__.Futbolcu object at 0x000000B31C4CADF0> : istediğimiz formatta yazdırmadı, bu bir sonraki dersimizin videosu
print(futbolcu3.isim)                   #AA

print(futbolcu1 > futbolcu2)            # False

# yani sizin oluşturacağınız class, direkt toplama veya çıkarmaya müsait olmayabilir. siz onu kendiniz tanımlayabilirsiniz.
# ek bilgi: object clası, tüm nesnelerin türediği clastır.
# bu fonksiyonlar neden var?
#  kendi clasınızda kendi işlemlerinizi tanımlayabilmeniz için var.
# bir sonraki dersimizde bu metotların en çok kullanılan iki tanesini işleyeceğiz.
