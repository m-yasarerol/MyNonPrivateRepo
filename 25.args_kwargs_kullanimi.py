# phyton ileri seviye fonkisyonlar, *args, **kwargs kullanımı
# nesne yönelimli programlamanının sonlarına kadar geldik ama kalan kısmı anlamamız için fonksiyonlar hakkında ileri düzey denebilecek konuları anlamamız gereliyor.
# fonksiyonlarla ilgili biraz daha ileri düzey özelliklerden ve kullanımlardan bahsedeceğiz.
# bu günkü konumuz fonksiyonların nasıl parametre aldığı ile ilgili
def kuvvet_al(x,y):                     #pozitional arguments
    return x ** y

print(kuvvet_al(3,4))                   #81>> bu bizim zaten bildiğmi bir şey
# burada benim parantezimin içine yazdığım 2 parametre var, 3 x'in yerine geçiyor, 4 y'nin yerine geçiyor ve yazdırıyor. 
#dolayısıyla bu argümanlarda sıralamanın önemi var, bunlara "pozitional arguments" denir
# bu fonk. sadece bir sayı girersem çalışmaz. üç sayı girersem yine çalışmaz.
# dolayısıyla biz pozitional arguments denilen parametrelerden kullanıyorsak, hepsi tam olarak girilmeli, eksik girilse de fazla girilse de çalışmaz.

# başka bir arguman tipine bakalım
def bilgi_ver(ad,soyad,yas = "girilmedi"):      #keyvord argumend
    return f"Ad: {ad}  Soyad:{soyad}  Yas:{yas}"
print(bilgi_ver("Ali","Çalışkan",23))   #Ad: Ali  Soyad:�al��kan  Yas:23
# buraya yaş girmezsek hata verir, ama fonksiyona yas= girilmedi olarak varsayılan değer tanımlarsan sorun olmaz, bu tip parametrelere "Keyword argument" denir

# ben burda adını ve yaşını girmek istersem, soy adını girmek istemezsem ne yapacağım?
def bilgi_ver2(ad = "girilmedi",soyad = "girilmedi",yas = "girilmedi"):      #keyvord argumend
    return f"Ad: {ad}  Soyad:{soyad}  Yas:{yas}"
print(bilgi_ver2("Ahmet",yas=23))       #Ad: Ahmet  Soyad:girilmedi  Yas:23 >> özellikle yaş olarak belirtmeseydin soy ada 23 yazardı
print(bilgi_ver2())                     #Ad: girilmedi  Soyad:girilmedi  Yas:girilmedi
# pozitional arguments>> eksiksiz ve fazlasız olarak girilmeli
# keyword arguments >>varsayılan değerleri var, girebilirsin veya girmeyebilirsin
# bunlar bildiğiniz şeylerdi

# bir fonk. kaç tane parametre gireceğimizi bilmiyorsak yıldız parametresini gidereceğiz
# *args dediğinizde, istediğiniz kadar parametre kullanabilirsiniz.
def topla2(x,y):
    return x + y

def topla3(x,y,z):
    return x + y + z
    
def topla(*args):
    for arg in args:
        print(arg)
    print(type(args))

topla(1,2,3,4,"Phyton", True)           #(1, 2, 3, 4, 'Phyton', True)>> hepsini aldı
                                        #<class 'tuple'>
# *args ifadesi: istediğin kadar parametre girebilirsin, ben onları alıp demet olarak depolayacağım anlamına geldi

# kaç sayı gelirse gelsin çarpama yaptıralım
def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    return carpim
print(carp(2,3,5))                      #30

# kaç sayı gelirse gelsin ortalama alalım
def ortalama(*args):
    return sum(args) / len(args)
print(ortalama(5,8,10,11))              #8.5
# yani args ifadesi istediğin kadar parametre girebilirsin anlamına gelir

def selamla(mesaj,*args):
    print(mesaj)
    for arg in args:
        print(arg)

print(selamla("Merhaba","Nasılsın",23,True))    # Merhaba >> mesaja girdi, kalan argsa gitti
                                                # Nas�ls�n
                                                # 23
                                                # True
                                                # None
# burada hem pozitional hem de args kullandık, pozitional arguments mutlaka girilmeli

def selamla(mesaj,*args):
    sonuc = ""
    sonuc += mesaj
    sonuc += " "
    for arg in args:
        sonuc += arg
        sonuc += " "
    return sonuc

print(selamla("Merhaba","Ali","Nasılsın"))      #Merhaba Ali Nas�ls�n 

# GELELİM İKİNCİ KISIMA
# **kwars: istediğin kadar keyword parametresi girebilirsin anlamına geliyor
def fonk(**kwargs):
    print(kwargs)
fonk(ad = "ali", soyad = "Çalışkan", yas = 34)  #{'ad': 'ali', 'soyad': '�al��kan', 'yas': 34}
# benim girdiğim keyword argumentleri sözlük olarak saklıyor, istediğin sayıda girebilirsin

def fonk2(zorunlu,*args,**kwargs):              # bu fonk. beden zorunlu olarak bir tane zorunlu parametre istiyor , onun haricinde istediğim kadar parametre yazabilirim, onun haricinde istediğim kadar keyword argument yazabilirim
    print(zorunlu)
    print("--------")
    for arg in args:
        print(arg)
    print("--------")
    for k,v in kwargs.items():
        print(k,v)
fonk2(2,3,4,5,6,7, ad = "Ali", yas = "23")      # 2 >>zorunlu
                                                # --------
                                                # 3
                                                # 4
                                                # 5
                                                # 6
                                                # 7 >args'n içine geldi
                                                # --------
                                                # ad Ali
                                                # yas £ kwars'ın içine geldi

# bu ne işime yarar, decoratoru kullanırken daha iyi anlayacağız
# bir * koyman kargs olduğunu ifade eder, "args" yerine başka bir isim de yazabilirsin.
# iki ** koyman kwkargs olduğunu ifade eder, "kwargs" yerine başka bir isim de yazabilirsin.
