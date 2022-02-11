# ohytonda veri yapılarını incelemeye devam ediyoruz. bu dersimizde incelleyeceğimiz veri yapısı sözlükler.
# Sözlük nedir?
# Sözlük nasıl oluşturulur?
# Sözlük nasıl yazdırılır?
# Sözlükte verilere nasıl erişilir?
# Sözlükte veriler nasıl değiştirilir?
# Sözlükte birden fazla alan nasıl değiştirilir?
# Sözlükte birden fazla alan nasıl silinir?
# keys ve values ve items metotları
# Sözlüğü for döngüsü yardımıyla nasıl yazdırabiliriz?
# "isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]
# "book" : "kitap", "black": "siyah", "cat" : "kedi"
# günlük hayatta kullandığımız sözlüğe çok benzer. Yani seiz eğer bir ingilizce türkçe sözlük alsaydınız book: kitap olarak yazacaktır. Bunlardan birincisi kelimenin ismi, ikincisi onun anlamı olacaktır.
#phytonda da aynı mantık. ilk kelime key ikincisi value olarak tanımlanır.


kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
# virgüller elemanları birbirinden ayırır. burada ilk elemanımın keyi isim, ona karşılık gelen veri ali,
# ikinci keyim yaş, ona karşılık gelen veri 20 (int)

#ilk söylemek istediğim: sözlüklerdeki anahtarlar string veya int olmak zorunda, ancak value dediğimiz kısım her şey olabilir (string, int, küme , liste vb..)
#key, yani elemanın ilk bileşeni mutlaka int veya str olmak zorunda
# peki sözlükteki verileri nasıl görüntüleyebiliriz. 

kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi)     #{'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}

# ancak ben bunun tamamını değil de sadece isim kısmını yazdırmak istersem?
# aynı listeleri yazdırıken kullandığım gibi köşeli parantezi açtım, ancak bunun içine bir index yazmayacağım çünkü sözlük yapısında index diye bir kavram yok, onun yerine verilerin anahtarları var. onu yazamam lazım. yani  köşeli parantezin içine:
#  "kişinin isim anahtarına karılık gelen veriyi yazdır" dersem;
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi["isim"])     #ali

kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi["cinsiyet"])     #n >> kişi sözlüğündeki cinsiyetin karşılığını getirir.

# yani aynen listeleri yazdırırken kullandığım gibi köşeli parantezleri açıyorum ancak içine index değil , anahtarı yazıyorum. o da bana bunun karşılığını döndürüyor. yani elemanlarımıza bu şekilde teker teker ulaşabiliyoruz.

# SÖZLÜĞÜ GÜNCELLEME
# peki, elemanlarımızı nasıl değiştirebiliriz?
# mesela ben buradaki kişinin ismini ali değil de ahmet yapmak istiyorum.
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi)     #{'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}
kisi["isim"] = "Ahmet"
print(kisi)     #{'isim': 'Ahmet', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}
# aynı elemana erişmek istiyormuş gibi köşeli parantez açtım, "isim" anahtarına eriştim, ve onu ali değil de ahmet yaptım.
# aynı listelerdeki atama gibi (= yardımıyla) sözlüğümüzdeki elemanları da güncelleyebiliyoruz.

#peki aynı anda iki alanı güncellemek isteseydim:
# hem ismi hem de  yaşını güncelle:
#update fonksiyonunu kullanacağım.

kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi)
# output: {'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}
kisi.update({"isim" : "Ahmet", "yas": 30})
print(kisi)
# output: {'isim': 'Ahmet', 'yas': 30, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}
#benim yazmadığım alanlarda herhangi bir değişiklik olmadı
#yani aynı anda birden fazla alanı güncellemek isteiyorsanız update fonksiyonundan yararlanabilirsiniz.

# peki sözlüğümüzden bir alanı nasıl silebilirim?
# silmeden önce kişiye bir id alanı ekleyelim:
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi)
# output:{'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}
kisi["id"] = 12345                    
print(kisi)
# output: {'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m'], 'id': 12345}

# id yi silmek istersem? "del" fonksiyonundan yararlanacağım.
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
kisi["id"] = 12345
print(kisi)      #{'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m'], 'id': 12345}
del kisi["id"]
print(kisi)     #{'isim': 'ali', 'yas': 20, 'cinsiyet': 'n', 'hobiler': ['sinema', 'konser', 'yaz�l�m']}
# del yazdım, sözlüğün ismini yazdım, içine de silmek istediğim anahtarı yazdım.
# del fonksiyonu ile istediiin herhangi bir alanı silebilirsin.

# biz diğer veri yapılarımızı for döngüsü ile yazdırmıştık, peki sözlüğümüzü nasıl for döngüsü ile yazdıracağız?
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
for x in kisi:
    print(x)    #isim
                # yas
                # cinsiyet
                # hobiler
# Bana anahtarları yazdırdı, ben bunların değelerini de yazdırmak istersem:
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
for x in kisi:
    print(kisi[x])  #ali
                    # 20
                    # n
                    # ['sinema', 'konser', 'yaz�l�m']
#  süreç şöyle çalıştı:
# - x önce isim oldu, sonra isim anahtarının değerini yazdırdı,
# - x yas oldu, sonra yas anahtarının değerini yazdırdı,
# - x önce cinsiyet oldu, sonra cinsiyet anahtarının değerini yazdırdı,
# - x önce hobiler oldu, sonra hobiler anahtarının değerini yazdırdı,

# yani eğer biz bir for döngüsü ile herhangi bir sözlüğü yazdırmak istersek, for döngüsündeki değişken (ilk yazılan x) anahtarların yerine geçiyor, değerlerin yerine geçmiyor.

# biz bu sözlükteki sadece ve sadece anahtarları almak istersek:
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.keys())  #output: dict_keys(['isim', 'yas', 'cinsiyet', 'hobiler'])
# bunu çalıştırdığım zaman bana sadece keylerden oluşan bir liste döndürdü.

# peki ben sadece değerleri almak istersem, yani values dediğim kısımları almak istersem? bunu da values metodu ile yapacağım.
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.values())    #output: dict_values(['ali', 20, 'n', ['sinema', 'konser', 'yaz�l�m']])

# peki ben burdan isim ve ali verisini hem anahtar hem değer olarak almak istersem ne yapacağım?
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.items()) 
#output: dict_items([('isim', 'ali'), ('yas', 20), ('cinsiyet', 'n'), ('hobiler', ['sinema', 'konser', 'yaz�l�m'])])
# bana bunları ikili ikili eşleştirip getirdi yani isim, ali; yaş, 20

# isterseniz kisi.items() fonksiyonunu for döngüsü ile kullanabilirsiniz. ÖR:
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
for k in kisi.items():
    print(k)            #('isim', 'ali')
                        # ('yas', 20)
                        # ('cinsiyet', 'n')
                        # ('hobiler', ['sinema', 'konser', 'yaz�l�m'])    

#peki ya şöyle yaparsam:
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
for k,v in kisi.items():
    print(k,v)          #isim ali
                        # yas 20
                        # cinsiyet n
                        # hobiler ['sinema', 'konser', 'yaz�l�m']
# bakın ilginç bir şey oldu, bu for döngüsünde detaylı öğreneceğimiz bir şey ancak, kişi.items() bize ikili bir değer döndüğü için ben de burada 2 adet değişken kulllanabilirim, yani:
# k beninm anahtarım, v de beninm değişkenim, ikisini yan yana yazdırmış oldum.

# bitirmeden önce değinmek istediğim son bir şey daha var.
# peki ya sözlüğümüzde olmayan bir alanı görüntülemek istersem?
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi["id"])       # error!
# hata aldım çünkü sözlüğümüzde öyle bir anahtar yok. Dolayısıyla ona karşılk gelen bir değer de yok.
# peki ben herhangi bir alana ulaşmak istersem, ve bu alan sözlükte bulunmasa bile programın hata vermesini istemiyorsam;
# bunun için "get" fonksiyonundan faydalanacağım.
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.get("id"))   #output: none >> "none" hiç yok manasına gelir.

kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.get("isim")) #output: ali
# gördüğün gibi sözlükte bulunan bir anahtarı yazdırdığımda aynı normal erişmek istediğim gibi bana onun değerini döndürüri tek bir fark var, eğer erişmek istediğim eleman sözlükte yoksa bana "none " değerini döndürüyor.

# hatta none demesin de bulunamadı desin, ne yapacağım? ikinci bir parametre olarak "bulunamadı" yazalım bakalım ne olacak.
kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.get("isim", "bulunamadı"))   #output: ali >> ali yazdı, çünkü isim diye bir alan burda var.

kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.get("yas", "bulunamadı"))   #output: 20 >> 20 yazdı, çünkü yas diye bir alan da burda var.

kisi ={"isim" : "ali" , "yas" : 20, "cinsiyet" : "n" , "hobiler" : ["sinema", "konser", "yazılım"]}
print(kisi.get("id", "bulunamadı"))     #output: bulunamadı >> yani bu get metodunun içine virgül ile ayırıp yazacağım ikinci parametre, eğer aradığım anahtar, sözlükte yok ise vermesini istediğim mesajı ifade eder.

# evet arkadaşlar phytondaki sözlük yapısını işledik, temel düzeyde işimize yarayacak tüm metotları işledik, böylece temel veri yapılarını bitirdik, burdan sonra if yapsına geçeceğiz, işin eğlenceli kısmı diyebilirim. Temel veri yapılarını iyi anlamanızı tavsiye ederim çünkü sık sık kullanacağız.

