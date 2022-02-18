# phyton ileri seviye fonkisyonlar, iç içe fonksiyon kullanımı
# oldukça basit
def dis_fonksiyon():
    print("Dış fonksiyon çalışıyor")
    def ic_fonk():
        print("İç fonksiyon çalışyor")
    print("Dış fonksiyon sonlanıyor")

dis_fonksiyon()             # D�� fonksiyon �al���yor
                            # D�� fonksiyon sonlan�yor
# iç fonk.oluşturduk, ancak çalıştırmadğımız için yazmadı, çalıştıralım:

def dis_fonksiyon():
    print("Dış fonksiyon çalışıyor")
    def ic_fonk():          #<< oluşturuyorum
        print("İç fonksiyon çalışyor")
    ic_fonk()               #<< çalıştırıyorum
    print("Dış fonksiyon sonlanıyor")

dis_fonksiyon()             # D�� fonksiyon �al���yor
                            # iç fonksiyon �al��yor
                            # D�� fonksiyon sonlan�yor

# bir de parametreli bir şekilde yapalım
def hesaplamalar(x):
    def kare_al(a):
        return a ** 2
    def karekok_al(a):
        return a ** 0.5
    def faktoriyel(a):
        carpim = 1
        for i in range(1,a + 1):
            carpim *= i
        return carpim
    kare = kare_al(x)
    karekok = karekok_al(x)
    fakt = faktoriyel(x)
    return f"Karesi: {kare} Karekökü:{karekok} Faktöreiyel: {fakt}"

print(hesaplamalar(6))      # Karesi: 36 Karek�k�:2.449489742783178 Fakt�reiyel: 720
# 6, hem x'in hem a nın yerine geldi. a ' nın yerine ne koyarsan koy değişmez
print(kare_al(6))   # fonks.yona dışarıdan ulaşamıyorum. o fonksiyon hesaplamalar bloğunun içinde

def toplam_carpim(*args):
    def toplama(demet):         # dışarıya değer döndürmez
        return sum(demet)       #demetlerin toplamını veren fonksiyon
    def carpma(demet):
        carpim = 1
        for i in demet:
            carpim *= i
        return carpim
    return f"Toplamları: {toplama(args)} Çarpmları:{carpma(args)}"  # dışarıya değer döndürür.

print(toplam_carpim(1,2,5,8))   #Toplamlar�: 16 �arpmlar�:80
