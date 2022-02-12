#phyton yardımıyla dosyaları nasıl açarız okuruz veya yazarız, en sonra dosyayı nasıl kapatırız onları göreceğiz.
f = open("deneme.txt", "r")         #dosyayı açtım
icerik = f.read()                   #işlemler
print(icerik)
f.close()                           # kapat
# bu sıralama değişmiyor neredeyse.
# open dosyayı açmamı sağlar, dosya yerine yerine adresini de yazabilirdim.
# "r", read mode anlamına gelir. yani phytona bu dosyayı okuyacağımı söyledim. bir şeyler yazmaya çalışırsem hata verir
# "w" yazmaya yarar, okumaya çalışırsan hata verir
# ilk parametre dosyamın yolu, ikinci parametre hangi modda açmayı istediğim
# deneme.txt projemle aynı dosyada olduğundan tam adresini yazmama gerek kalmadı
# f.read(): dosyayı okur, içine herhangi bir şey yazmadığım için tüm dosyayı okur
# f.close(): açtığın dosyayı kapatır, eğer kapatmazsan bu dosya hafızada yer tutmaya devam eder. 10.000 müşterisi olan bir projede açtığın dosyayı kapatmazsın hafıza problemleri yaşarsın
# temel olarak iin akışı bu şekilde. ama pratikte şu şekilde kullanacağz:

with open("deneme.txt","r") as f:           #dosyayı aç, f olarak isimlendir. az önce yaptığmız işlemin neredeyse aynısı.
    icerik = f.read()
    print(icerik)
# aynı sonucu verdi

icerik2 = f.read()                          # eror: kapal bir dosyada çalışıyorsun dedi. yani yukarıdaki kullanımı dosyayı otomatik olarak kapatır. en büyük avantajı budur

with open("deneme.txt") as f:           
    icerik = f.read()
    print(icerik)
# açma moduna hiçbir şey girmesen de phyton varsayılan olarak "r " mdou ile açar

# dosyamızı satır satır okumak istersek:
with open("deneme.txt") as f:
    icerik = f.readlines()
    print(icerik)                           #['Dosyalarla �al�ma\n', 'Birinci k�s�m: dosyalar� a�ma\n']
# yani burada her  satırı bir eleman olarak algılar, onları bir listeye dönüştürüp bize sunar. her satır, bizim için listenin bir elemanıdır

with open("deneme.txt") as f:
    icerik = f.readlines()
    print(icerik)
    for satir in icerik:
        print(satir)        
# aralarda birer satır boşluklar oluştu, for döngüsünde print kullandığında bir parametre vermezsen phyton otomatik olarak enter olarak algılar.
# hem belge hem for entere basıyor. görelim:
with open("deneme.txt") as f:
    icerik = f.readlines()
    print(icerik)
    for satir in icerik:
        print(satir, end="")
#boşluklar giderildi.

with open("deneme.txt") as f:
    for satir in f:
        print(satir, end= "")
# satırları alt alta yazdı, yani phyton satır satır okuyor. direkt dosyamızın kendisini de for döngüsü ile satır satıryazabiliriz ya da satırları bir listeye çevirebiliriz.

with open("deneme.txt") as f:
    satir = f.readline()
    print(satir)                    #Dosyalarla �al�ma>> belgemin içerisinden sadece bir satır okudu

with open("deneme.txt") as f:
    satir = f.readline()
    print(satir, end= "")
    satir = f.readline()
    print(satir, end= "")
    satir = f.readline()
    print(satir, end= "")           # Dosyalarla �al�ma
                                    # Birinci k�s�m: dosyalar� a�ma
                                    # r modu: Okuma modu (Dosya yoksa hata verir)
# gördüğün gibi 3 satır yazdı, burada bir imleç mantığı var. dolayısıyla imlecin nerede kaldığına dikkat et
# peki imlecin nerede olduğunu unutursak ne yapacağız:

# tell: imlecin nerede olduğunu gösterir
with open("deneme.txt") as f:
    satir = f.readline()
    pozisyon = f.tell()
    print(satir + str(pozisyon))    #Dosyalarla �al�ma
                                    # 19>> imlec 19. karakterde bekliyor. bir daha readline dersem bundan sonraki satırı okuyarak devam edece

# peki imleci istediğim bir yere götürmek istersem?
# f.seek fonksiyonundan yararlanacağız
with open("deneme.txt") as f:
    icerik = f.readline()
    pozisyin = f.tell()             
    print(icerik + str(pozisyin))       
    f.seek(0)
    print(icerik)                   # Dosyalarla �al�ma
                                    # 19
                                    # Dosyalarla �al�ma
# aynı satırı okudu çünkü seek 0 dediğimde yine 0 satıra döndü

#read parametresine bir sayı girersem ne olur
with open("deneme.txt") as f:
    icerik = f.read(10)
    print(icerik)                   #Dosyalarla
# metin belgesinden ilk 100 karakter yazdı. bu nerede işime yarar? büyük dosyaları parça parça okumak veya taşımak daha mantıklıdır. dev dosyalardab bahsediyorum.

# arka arkaya çalıştırırsam ne olur?
with open("deneme.txt") as f:
    icerik = f.read(10)
    print(icerik, end= "") 
    icerik = f.read(10)
    print(icerik, end= "")
    icerik = f.read(10)
    print(icerik, end= "")          #Dosyalarla �al�ma
                                    # Birinci k�s�
# 10 karakter okudu, bir 10 daha okudu, sonra bir 10 daha okudu

# dosyanın sonuna kadar 10 ' ar karakter şeklinde okuyup ekrana yazalım
with open("deneme.txt") as f:
    okunacak_miktar = 10
    icerik = f.read(okunacak_miktar)     
    while len(icerik) > 0:              # okunacak bir harf kalana kadar devam eder
        print(icerik, end= "")
        icerik = f.read(okunacak_miktar)
# mesela 50 gb lik bir dosyan varsa bu şekilde parça parça okursun, daha verimli olur.

# dosyaları yazmaya başlayalım (dosya yokse o dosya bizim için oluşturulur)
with open("deneme2.txt", "w") as f:
    f.write("Hello world")
# klasörümde deneme2.txt isimli bir dosya açup içine "hello world" yazdı
# kodu tekrar çalıştırırsan dosyayı baştan oluşturur ve tekrar yazar. önceki dosya gider

# a modu burada önem kazanıyor. a modu append mod anlamna gelir, yani sonuna ekleme modu
with open("deneme2.txt", "a") as f:
    f.write("whats up?")
# sonuc olarak belgede "Hello worldwhats up " yazdı.
# w modunda çalıştırsaydım belgede sadece whats up yazardı.

#deneme.txt ' nin içeriğini deneme2.txt ye kopyalayalım
with open("deneme.txt", "r") as okunacak:
    with open("deneme2.txt", "w") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)
# okunacak olan içeri okudum, satır satr diğer belgeye yazdım

# şu şekilde de yapabilirdim:
with open("deneme.txt", "r") as okunacak:
    with open("deneme2.txt", "w") as yazilacak:
        icerik = okunacak.readlines()
        for satir in icerik:
            yazilacak.write(satir)
# aynı işlemi yaptı

# bir de png dosyası ile çalışalım, r ve q olmayacak çünkü bunlar metinsel ifadeler için, göster içerikler için wb, yani binary kullancağım. bunları bit bit oku gibi düşünebilirsin 
with open("phyton.png", "wb") as okunacak:
    with open("phyton2.png", "wb") as yazilacak:
        okunacak_miktar = 1024
        icerik = okunacak.read(okunacak_miktar)
        while len(icerik) > 0:
            yazilacak.write(icerik)
            icerik = okunacak.read(okunacak_miktar)
# büyük iso dosyası olma ihtimaline karşı miktar belirttim

# şöyle de yapabilirsin
with open("phyton.png", "wb") as okunacak:
    with open("phyton3.png", "wb") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)
# bu kod her zaman çalışmaz , çünkü her görüntü tek seferde okuyabileceğiniz kadar küçük olmayabilir.
