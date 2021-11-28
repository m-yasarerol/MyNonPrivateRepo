# tuple(demet) nedir?
# tuple ve list yapılarının farkı ve benzerlikleri
# "sarı", "mavi", "yeşil", "kırmızı", "siyah"
#bu günkü inceleyeceğimiz veri yapıları tuple ve set
# liste dersinden sonra çok kolay gelecek
# tuple listeye çok benzer, sadece bir temel farkı var desek yanlış olmaz, aynıı listede olduğu gibi elemanlarımı içine yazacağım, listeden tek fark normal parantez kullanacağız.
# normal parantez kullanmamız phytona bunun bir demet olduğunu söyler

demet = ("sarı", "mavi", "yeşil", "kırmızı", "siyah")
print(type(demet))      #<class 'tuple'>
print(len(demet))       #5 >> len, listedde kaç eleman olduğunu yazdırıyordu, gördüğün gibi demette de çalıştı
print(demet)            #('sar�', 'mavi', 'ye�il', 'k�rm�z�', 'siyah')

for renk in demet:
    print(renk)         #sar�
                        # mavi
                        # ye�il
                        # k�rm�z�
                        # siyah >> for döngüsü de aynı şekilde çalıştı.
    
# PEKİ, DEMET'İN LİSTELERDEN FARKI NEDİR? SADECE KÖŞELİ PARANTEZ DEĞİL TABİ Kİ
demet = ("sarı", "mavi", "yeşil", "kırmızı", "siyah")
demet[2] = "pembe"      #TypeError: 'tuple' object does not support item assignment/ tupple objesi nesne atamayı desteklemiyor.!
# eğer bir demetle çalışıyorsan demete herhangi bir eleman ekleyemezsin, silemezsin veya var olan herhangi bir elemanı değiştiremezsin/güncelleyemezsin, dolayısıyla bir demet nasıl oluşturulduysa öyle kalır
# yani demete elemanlarına değişiklik uygulayamadığımız listelerdir diyebiliriz.
# dolayısıyla listelerde olan appent, insert, remove gibi listenin kendisini değiştiren komutlar demetlerde yok
# bunun haricinde kullanımı, yazdırılması, elemanlara erişimi tamamen aynı.
# liste konusunu işlediğimiz için bunu kısa kesip asıl konumuz olan küme kavramına geçmek istiyorum

# KÜME
# biraz daha değişik bir veri yapısı, demetlerde de, demetlerde de elemanlarımız sıralı bir şekilde tutuluyordu ve her ikisinde de elemanların birer indeksleri vardı, o indexler sayesinde elemanlara erişebiliyordum yani:
# 0.index bir renk, 1. index bir renk şeklinde ilerliyordu, kümelerde bu yok. KÜMELER SIRASIZ BİR VERİ YAPISIDIR VE KÜMELERDE BİR ELEMAN YANLIZCA BİR KEZ BULUNABİLİR.
# listede bir listeye aynı elemanı 3-5 kez ekleyebilirsin ama kümeye ekleyemezsin, yazdırmaz. ör:
# küme parantezi {} ile kullanmamız phytona bir küme olduğunu söyler.
#kullanımı list ve demetten farklı değil.
küme = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
print(type(küme))       #<class 'set'> >>phyton bir küme olduğunu anladı
print(len(küme))        #5
print(küme)             #{'siyah', 'sar�', 'k�r�m�z�', 'mavi', 'ye�il'}
for renk in küme:
    print(renk)         #mavi
                        # ye�il
                        # sar�
                        # k�r�m�z�
                        # siyah
#kümeler sırasız bir veri yapısı olduğundan, her çalıştırdığımda renkleri farkl sırada yazdırıyor! dolayısıyla bir kümeye elemanları hangi sırada eklediğimin bir önemi yok.
#kümelere eleman ekleme/silme işlemlerini nasıl yapabilirim?
#apent: listelerde kullandığımız bir metottu, listenin sonuna eleman ekliyordu, solayısıyla kümeler sırasız tutulduğundan kümelerde appent metodu yok.
# appent yerine "ADD" metodunu kullanacağız
küme = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
print(küme)             #{'k�r�m�z�', 'siyah', 'ye�il', 'sar�', 'mavi'}
küme.add("pembe")
print(küme)             #{'k�r�m�z�', 'pembe', 'siyah', 'ye�il', 'sar�', 'mavi'} >> ortaya bir yere eklendi, kümelerde sıralamak yok.

#kümelerden eleman silmek
#kümeden "sarı" elemanını siliniz.
#REMOVE metodunu kullanacağız.
küme = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
küme.remove("sarı")
print(küme)             #{'mavi', 'ye�il', 'siyah', 'k�r�m�z�'}

#peki kümede olmayan bir elemanı silmek istersek ne olur?
küme = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
küme.remove("gri")
print(küme)             #eror!
# biz kümelerden bir eleman silmek istediğimizde, o eleman kümede yoksa, biz hata almak istemiyorsak yani programın çalışmasına devam etmesini istiyorsak remove fonksiyonunu kullanamayız.

# o zaman kümelerdeki diğer bir fonksiyon olan "DİSCART" metodunu kullanacağız.
küme = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
küme.discard("gri")
print(küme)             #{'k�r�m�z�', 'sar�', 'ye�il', 'siyah', 'mavi'}
#yani kümemizde gri olmadığı için herhangi bir şeyi silmedi ancak hata da vermedi.

# KÜMELERDEKİ KESİŞİM VE BİRLEŞİM
# günlük hayatta kullandığımız kesişim ve birleşim ile aynı

kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
#bu iki kümede birden bulunan elemanları, yani ortak elemanları bulmak istersem: (bunun karşılığı kesişim
#intersection metodunu kullanacağız
print(kume1.intersection(kume2))    #{'ye�il', 'sar�', 'mavi'} >> ortak elemanları yazdırır.
#print(kume1.intersection(kume2)) = print(kume2.intersection(kume1)) == A kesişim B = B kesişim A
 
#birleşim: intersection yerine union metodunu kullanırız.
kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
print(kume1.union(kume2))       #{'mavi', 'sar�', 'ye�il', 'beyaz', 'gri', 'k�r�m�z�', 'siyah'}
#tekrar eden elemanları bir kez yazdırır. kumenin elemanları eşsizdir. aynı eleman ı2 kez yazsan bile bir kez yazdırır.

#fark: küme 1 de olup küme 2 dde olmayan rekler: difference metodu
kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
print(kume1.difference(kume2))  #{'siyah', 'k�r�m�z�'} >>küme 1 başta yazdığı için, küme 1 de olup küme 2 de olmayan elemanları alır.

kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
print(kume2.difference(kume1))  #{'gri', 'beyaz'} >> küme 2 de olup küme 1 de olmayanlar.

#en son işlemek istediğim anahtar kelime "in" anahtar kelimesi
# in anahtar kelimesi bizim herhangi bir elemanımızı bir kümede bir listede, kümede, demette var olup olmadığı anlamına gelir.
kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
print("sarı" in kume1)           #true >>sarıı elemanı küme 1 de olduğu için true değerini döndürdü.

kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
print("beyaz" in kume1)           #false

kume1 = {"sarı", "mavi", "yeşil", "kırımızı", "siyah"}
kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}
print("beyaz" in kume1.union(kume2))           #true >> beyaz elemanı bu kümelerin birleşiminde var ise true, yok ise false değerini döndürür

#in değerini döngülerde de çok kullanacağız.

#ben boş bir liste, küme, demet oluşturmak istiyorsam ne yapabilirim?

#bunların ikisi de boş birer listedir.
bosliste1 = []
bosliste2 = list() 

#bunların ikisi de boş birer demettir.
bosdemet1 = ()
bosdemet2 = tuple

boskume1 = set()
boskume2 = {}           # bu bir sözlüktür. küme parantezlerini bu şekilde kullanırsan boş bir küme oluşturmaz, bakalım ne oluşturmaz. bakalım ne oluşturmuş:
print(type(boskume2))   #<class 'dict'> >> dict oluşturdu. henüz bu yapıyı bilmiyoruz. bir sonraki derste işleyeceğiz.

#boş demet ve küme oluşturmak için iki metodunuz var ama boş küme oluşturmak için sadece bir metodunuz var.
# bu farkı da bilin sonra nerede hata var diye aramayın

phyton = set("PHYTON")
print(phyton)
#soru: bizim kümemizde sadece phyton isminde bir eleman mı olacak yoksa bu harflerin her birisi ayrı ayrı eleman mı olacak?
#output:{'P', 'T', 'O', 'H', 'N', 'Y'}
#elemanlarına parçaladı ve o elemanları ayrı ayrı kümeye çevirdi.
#set fonksiyonunun içine kümeye çevrilebilecek, elemanlarına parçalanabilecek bir veri girerseniz mutlaka onu elemanlarına parçalar bir kümede birleştirir, bir liste veya bir demet girersen bile.
#Örnek:
phyton = set([1,2,3,4,5])
print(phyton)       #{1, 2, 3, 4, 5} >>içine bir liste girdim, onu da kümeye çevirdi.

phyton = set({1,2,3,4,5})
print(phyton)       #{1, 2, 3, 4, 5} >>içine bir demet girdim, onu da kümeye çevirdi.

#sözlük veri yapısını işledikten sonra if bloklarına geçececeğiz, daha eğlenceli dersler işleyeceğiz diye düşünüyorum.


