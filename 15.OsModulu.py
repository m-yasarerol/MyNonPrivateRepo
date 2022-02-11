#önemli modülleri işlemeye devam ediyoruz.
# os modülünden bahsedicem
#os modülü : işletim sistemimiz ile ilgili birtakım fonk. barındırır.
# ne işe yarar? os modülü yardımıyla:
# > dosya sistemimizde gezinebiliriz
# > klasörlerin içeriğini görüntüleyebiliriz
# > dosyalarımızı yeniden adlandırabiliriz
# > klasörlere ayırabiliriz.
import os
from stat import ST_ATIME
print(os.getcwd())                      #c:\Users\HP655\Desktop\phyton dersleri : nerede olduğumuzu gösterir. Çalışan, aktif olan dizini gösterir, bir parametre almaz.
os.chdir("/Users/HP655/Desktop/Yeni")   # klasör değiştirmeye yarar
print(os.getcwd())                      #c:\Users\HP655\Desktop\Yeni
# chdir e string olarak bir klasör adresi girmelisin

# bir klasörün içeriği nasıl görüntülenir
print(os.listdir())                     #[] >> klasör boş
# içine herhangi bir parametre yazmazsan içinde bulundupun klasörün içeriğini gösterir
print(os.listdir("/Users/HP655/Desktop/phyton dersleri"))    
#['01.strings.py', '02.IntegerAndFloat.py', '03.01.listsalistirmalar.py', '03.lists.py'
# gördüğün gibi pek okunaklı değil. for döngüsü ile yazdıralım
for dosya in os.listdir("/Users/HP655/Desktop/phyton dersleri"):
    print(dosya)   
# 01.strings.py
# 02.IntegerAndFloat.py
# 03.01.listsalistirmalar.py
# 03.lists.py

# peki nasıl yeni bir klasor 
import os
os.chdir("/Users/HP655/Desktop/Yeni")   # masaüstümde "yeni" isimli klasöre gittim
os.mkdir("yeni klasör 1")               # yeni klasör 2 isimli bir dosya açtum

# iç içe birden fazla klasöt oluşturmak istersem
os.makedirs("Deneme1/deneme2/deneme3")

#klasör silmek
os.rmdir("Yeni")
#rmdir tek bir klasör siler

# iç içe olan klasörleri silelim
os.removedirs("Deneme1/deneme2/deneme3")
#bu fonksiyonlarla sadece boş olan klasörleri silebilirsiniz.

# dosya silmek
# klasör 1 deki dosyayı sil
import os
os.chdir("/Users/HP655/Desktop/Yeni/yeni klasör 1")
silinecek = os.listdir()[0]
print(silinecek)                #Yeni Metin Belgesi.txt
os.remove(silinecek)

# mkdir: tek klasör yapan fonksiyon
# makedirs: iç içe klasörler yapar
#  rmdir: bir klasör siler
# removerdirs: iç içe klaösr siler( içi boş olmalı)
# remove: dosya siler

# yeniden adlandırma fonksiyonuna değienceğiz.
import os
os.chdir("/Users/HP655/Desktop/Yeni")
#os.mkdir("danama3.docx")
os.rename("danama3.docx","Deneme3.docx")
# zaten bu dosyanın içinde olmasaydım adres vermem gerekirdi
# 2 parametre alır, değiştirmek istediğin klasör ve yeni ismi
# rename fonkisyonunu bir dosyayı başka bir yere taşımak için de kullanabilirsin. 2. parametreye taşımak istediğin adresi girmelisin.

#stat parametresi dosya hakkında bilgi almamızı 
import os
os.chdir("/Users/HP655/Desktop/Yeni")
print(os.stat("Deneme3.docx"))
# output: os.stat_result(st_mode=16895, st_ino=24206847997384505, st_dev=2753849356, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1644587784, st_mtime=1644587784, st_ctime=1644587784)
# bunlardan bir tanesi dosya boyutu, bir tanesi ne zaman oluşturulduğu gibi özellikler yer alıyor.
# şu şekilde detaylarına ulaşabiliriz:
import os
from datetime import datetime
os.chdir("/Users/HP655/Desktop/Yeni")
print(os.stat("Deneme3.docx").st_atime)         # en son ne zaman erişildiğini belirtir.
                                                #1644587784.6612575>> ben zaman yazmasını beklerken o bana acayip şeyler yazdı. bir önceki dersten hatırlayın zaman modülünü nasıl okunabilir hale getiriyorduk?
zaman = datetime.fromtimestamp(os.stat("Deneme3.docx").st_atime)
print(zaman)
                                                #2022-02-11 16:56:24.661258 >> phytondan gelen veriyi okunabilir hale getirdik. bu dosyanın son ulaşım tarihi buymuş

#st_size dosyanın boyutunu verir
#st_mtine son değiştirilme tarihini verilir
# os.stat fonksiyonu da dosyamızın özelliklerine erişmemizi sağladı

# walk: bulunduğumuz dizinden başlayıp içinde ne var ne yok listeleyen bir fonksiyon
# mesela 3 adet iç içe klasör var , hepsinin içini listeler
# kullanımı
# hem klasörleri hem de içeriklerini görüntüler
# içine parametre olarak adres alır

import os
os.chdir("/Users/HP655/Desktop/Yeni")
for gecerli_klasör, icindeki_klasörler, icindeki_dosyalar in os.walk("/Users/HP655/Desktop/Yeni"):
    print("Geceli klasör:" , gecerli_klasör)
    print("İcindeki klasörler", icindeki_klasörler)
    print("icindeki dosyalar", icindeki_dosyalar)
# Output
# Geceli klas�r: /Users/HP655/Desktop/Yeni
# �cindeki klas�rler ['Deneme3.docx', 'yeni klas�r 1']
# icindeki dosyalar []
# Geceli klas�r: /Users/HP655/Desktop/Yeni\Deneme3.docx
# �cindeki klas�rler ['c klasörü']
# icindeki dosyalar ['a_bengesi.docx']
# Geceli klas�r: /Users/HP655/Desktop/Yeni\Deneme3.docx\vikvik
# �cindeki klas�rler []
# icindeki dosyalar ['Yeni Metin Belgesi.txt']
# Geceli klas�r: /Users/HP655/Desktop/Yeni\yeni klas�r 1
# �cindeki klas�rler []
# icindeki dosyalar []
# bir ağaç olarak düşünürsek gövdeden başlayıp dallara dopru ilerler


# şimdi dosya yolu oluşturan bir fonksiyondan bahsedeceğim
import os
print(os.path.join("Deneme a", "Deneme b", "Deneme c")) #Deneme a\Deneme b\Deneme c
# ne işimize yarar? : biz buradaki isimleri teker teker programın çalışması esnasında değişik yerlerden alacağız. İstediğimiz dosyaya ait dosya yolu oluşturacağız.
# bunun şöyle bir kullanımı var, bu isimlerden herhangi birinin başına slash / koyarsan, ondan öncekileri görmez, slaın olduğu yerden başlar

# isfile : bu bir dosya mı? kontrol eder
print(os.path.isfile("/Users/HP655/Desktop/Yeni"))      # False: çünkü bu bir klasör ismi, dosya adresi olsaydı true yazardı
# nerede kullanacağız?: bir program hazırlayacağız, dosyaları uzantılarına göre listeleyecek, burada dosyaları es geçmesi gerekecek

print(os.path.isdir("/Users/HP655/Desktop/Yeni"))      # True: çünkü bu bir klasör ismi, dosya adresi olsaydı false yazardı

#splitext : dosya uzantılarını elde etmek için faydalanacağız
print(os.path.splitext("/Users/HP655/Desktop/Yeni"))    #('/Users/HP655/Desktop/Yeni', '') >> uzantı yok
#bunu da az önce bahsettiğim uygulamada kullanacağız

# bundan sonraki videomuza bu os modülünü kullanarak bir proge geliştireceğiz. bu proje: bir klasörde bulunan değiik uzantılardaki dosyaları uzantılarına göre sıralayacak
# bir sonraki uygulamamızda dosyaları oluşturulma tarihlerine göre klsörlere ayıracak, bu uygulama kalabalık bir indirilenler klaösründe çok işe yarayabilir
# tavsiyem oraya gelmeden önce iyi bir tekrar edin.
