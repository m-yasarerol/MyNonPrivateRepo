# MyNonPrivateRepo
# stringler, metinsel veriyi tutan kavramlardır.
# string ifadeler tırnak içinde yazılır.
from typing import NamedTuple


print  ("hello world")
print("Hello world" + " my world")
print ('merhaba')
# phyton string ifadenin "ali" de bittiğini düşündü:
#print ('Ali'nin evi)
# "\" kullanırsam, örnekte görüldüğü gibi buna kaçış karakteri denir. phyton " benden sonra gelen karakter stringi bitiren kesme işareti değil, alelade bir kesme işareti" olarak algılar.
# yani "\" kendisinden sonra gelen karakterin özel bir karakter olmadığını belirtir.
print ('Ali\'nin evi')

print ("merhaba dünya")
# peki ya merhaba dünyayı alt alta yazmak isteseydik:
# yani çok satırlı metinlere geçiyoruz.
print("""Merhaba
dünya""")
# bu şekilde 3 tırnağı açtıktan sonra istediğin kadar satır kullanabilirsin.

#print edeceğimiz ifadede bazı özel ifadeler bulunabilir.
#örnek:
print("merhaba\ndünya")
#\n ifadesi yeni bir satır anlamına geliyor.

#önce merhaba yazıcak, sonra "tab" a basıcak, sonra dünyaya geçicek
#\t ifadesini tab aralığı olarak algılar.
print("merhaba \tdünya")

# bu stringleri hep elimizle mi yazacağız? uygulama geliştirirken bazı ifadeleri bilgisayarın aklında tutmasnı isteyeceğiz.
# bu verileri aklında tutan birimlere de değişkenler denir.
#ör:
mesaj = "Merhaba dünya"
print(mesaj)

#iki farklı değişkeni bir arada yazdırma:
mesaj1 = "merhaba"
mesaj2 = "dünya"
print(mesaj1 + " " + mesaj2)

# bir stringin içerisinde belirli bir harfi nasıl yazdırabiliriz.?
print(mesaj1[1])
# köşeli parantez içinde herhangi bir sayı yazarsam, o sayıya karşılık gelen harfi verir. Ama bilmen gereken bir şey var. Yazılım dilleri saymaya sıfırdan başlar. Buna da "index" denir.

#peki ya "-2" ye bakarsam?
print(mesaj1[-2])
#"-1" en sonu gösterir. "-2" ise ondan bir önceki karakteri yazdırır.
#bilmemiz gereken, köşeli parantez bize istediğimiz herhangi bir değeri geri döndürür.

#peki ya kelimenin ortasından bir kısım yazdırmak istersem?
mesaj1 = "merhaba"
print(mesaj1[0:4])
#"0" ile harfimizdi zaten. yanında "4" koyarsak "0 ve 4." karakterin arasını yazdırır. Ama bilmen gereken bir şey var..
# birinci sınır dahil, ikinci sınır dahil edilmez. (sonuç "merh" )
# phyton' da hemen hemen her yerde bu kural geçerlidir. İlk sınırı dahil eder. ikinicisini etmez.

mesaj1 = "merhaba"
print(mesaj1[::])
# bu şekilde ifade edersen stringin en başından en sonuna kadar alır. (sonuç "merhaba")

mesaj1 = "merhaba"
print(mesaj1[::2])
# ilk karakterden başlar, ikişer ikişer yazdırır. yani yazdırdığı karakterler 0-2-4-6.. şeklinde ilerler. (sonuç "mraa")

mesaj1 = "merhaba"
print(mesaj1[::-1])
# en son parametreyi -1 yaparsan versayılan parametrelerin yerlerini değiştirir. yani merhabayı tersten yazdırır. (sonuç "abahrem")

#upper metodu büyüh harflerle yazdırır
mesaj3 = "phyton"
mesaj4 = "öğreniyorum"
print(mesaj3.upper())
#sonuç: PHYTON
# bu bize yeni bir metin döndürür, mesaj içeriğini değiştirmez.

mesaj3 = mesaj3.upper()
print(mesaj3)
#bu şekilde mesaj değişkenini her yazdırdığımızda büyük harfler ile yazılsın istiyorsan yukarıdaki şekilde tanımlayabilirim.
#sonuç: PHYTPON
mesaj3 = mesaj3.lower()
print(mesaj3)
# gördüğün gibi büyüttüğüm bir mesajı sonradan küçültüp ekrana küçük harfler ile yazdırabilirim.

mesaj3 = mesaj3. capitalize()
print(mesaj3)
# capitalize, baş harfini büyütür.

mesaj5 = "yapay zeka"
print(mesaj5.startswith("ya"))
#bu metot, bir metinin herhangi bir ifade ile başlayıp başlamadığını kontrol etmek için kullanılır
#bu metodu nerede kullanabilirim?
#diyelim ki isimlerden oluşan bir listemiz var, ismi "a" ile balayanları ayıklamak istediğimizde kullanabiliriz.
#Sonuç:(true)

print(mesaj5.endswith("ka"))
# aynı şekilde, bu metodumuz da stringin herhangi bir ifade ile bitip bitmediğini kontrol etmek için kullanılır.
#Sonuç:(true)

print(len(mesaj5))
#önemli bir metottur. bir mesajın kaç karakterden oluştuğunu gösterir.
#not: saymaya sıfırdan başladığını unutma.

print(len (mesaj5 + " " + mesaj4))
#sonuç: 22
# gördüğün gibi toplam işreti phytonda string ifadeleri yan yana yazmak için kullanılır.

print("PHYTON " * 10)
#phyton ifadesini 10 kez ard arda yazar.

isim = "yaşar"
yas = "20"
print("{} , {} yaşındadır.".format(isim,yas))
#fotmatın ilk değişkeni birinci kümenin içine, ikinci değişken ikinci küme parantezin içine yazılır. bu şekilde sürekli "+" ifadesini kullanmak zorunda kalmazsın. Muhteşem değil mi?
#mesela bir uygulama yazdın, 100 kişinin isim ve yaş bilgilerini yazdıracaksın, teker teker + koymayacaksın tabiki. Böyle bir yapı kullnacaksın.
#sonuç: yaşar, 20 yaşındadır.

isim2 = "Abdullah"
mesaj6 = " Selam gönderdi"
print(" {} , sana {} ".format(isim2,mesaj6))
#sonuç: abdullah, sana selam gönderdi, format değişkenlerinin sırası önemli.

#bunu yapmanın şöyle bir yöntemi daha var.
print(f" {isim2} {mesaj6} sana")
#"f" phytonda özel bir kalıptır. gördüğün gibi f kullanarak direkt olarak kümpe parantezine adres verebildim. çünkü phyton onların birer değişken olduğunu hemen anladı.
#sonuç: abdullah selam gönderdi sana.

#DERS SONU, STRİNGLER EN ÖNEMLİ VERİ TİPLERİMİZDEN BİR TANESİDİR.
#HANGİ PROJE GELİŞTİRİRSENİZ GELİŞTİRİN MUTLAKA BİR STRİNG KULLANIRSINIZ.
#İLK 3-4 DERS MOTİVASYONUNU YÜKSEK TUT. İLK DERSLERİ TEK BAŞINA KENDİ KENDİ KENDİNE KULLANAMAZSIN (ÖR: STRİNG İFADELER)
#"BUNU ÖĞRENDİM NE OLDU ŞİMDİ NEREDE KULLANACAĞIM" DİYE DÜŞÜNME, SABIRLI OL, BİRKAÇ DERS SONRA KENDİ BAŞINA PROJELER OLUŞTURABİLECEKSİN.
# NASIL ALIŞTIRMA YAPABİLİRİM? DİYE DÜŞÜNÜRSEN BU NOKTADA PROJECT ÖGELER KONUSU BİZİM İÇİN ÖNEMLİ.
