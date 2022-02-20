# filter fonksiyonu
# ne işe yarar? bir listeyi belirli koullara göre filtrelememizi sağlar. peki bunu nasıl yapar? 
# filter fonksiyonu da map fonksiyonu gibi bizden parametre olarak bir fonk. ve bir liste alıyor. ancak burada fonksiyonum, true veya false değer
# döndüren bir fonksiyon olması gerekiyor. ve o listedeki elemanları teker teker bu fonksiyona gönderiyor, true değerini döndüren elemanlarla
# yani bizim istediğimiz koşulu sağlayan elemanlar ile yeni bir liste oluşturuyor. 

liste = [1,2,3,5,6,8,11,17,123,101]
# ben bunları belirli kurallara göre filtreleyeceğim
# 1- buradaki çift sayıları almak istersem: bir tane fonk. oluşturmalıyım ve bu fonk. çift sayılar için true, tek sayıları için false değeri döndürmeli.
def cift_mi(x):
    if x %2 == 0:       # bu sayının 2 ye bölümünden kalan sıfır ise:
        return True
    return False
ciftler = list(filter(cift_mi,liste))
print(ciftler)          #[2, 6, 8]

# 2- listedeki iki basamaklı elemanları filtrele:
def iki_basamakli(x):
    if x >= 10 and x <= 100:
        return True
    return False
iki_basamaklilar = list(filter(iki_basamakli,liste))
print(iki_basamaklilar) #[11, 17]
# filterde de map gibi bir fonksiyon ve bir liste gönderiyorum ancak burada gönderdiğim fonksiyonun true veya false değeri döndürmesi gerekiyor. True değerini döndürenler ile yeni bir liste oluşturuyorum.

# 3- ilk iki örneği lambda ile yazınız.
# 3.1
ciftler2 = list(filter(lambda x : x %2 == 0,liste))
# 3.2
iki_basamakli2 = list(filter(lambda x : x >= 10 and x <=100,liste))
# yukarıdaki iki kod da aynı sonucu verir.

# 4- aşağıdaki kelime listesinden sadece "a" ile başlayanları filtrele
kelimeler = ["ayna","ahmet","ama","kalem","defter","kazak","son"]
a_ile_baslayanlar = list(filter(lambda kelime: kelime.startswith("a"),kelimeler))
print(a_ile_baslayanlar)        #['ayna', 'ahmet', 'ama']

# 5- kelimeler listesinde içinde "a" geçen elemanları filtrele
icinde_a_gecenler= list(filter(lambda kelime: "a" in kelime,kelimeler))     # karşılaştırma ifadesi
print(icinde_a_gecenler)        #['ayna', 'ahmet', 'ama', 'kalem', 'kazak']

# 6- palindromları listele, palindrom, baştan ve sondan okunduğunda aynı olan kelimeleri ifade eder.
palindromlar = list(filter(lambda kelime: kelime == kelime[::-1],kelimeler))
print(palindromlar)             #['ama', 'kazak']

# 7- aşağıda bulunan karışık bir veri yapısına sahip listenin içerisindeki string ifadeleri listele.
liste = [1,2,(1,2,3),True,"string","örnek",{1,2,4}]
stringler = list(filter(lambda x : isinstance(x,str),liste))
print(stringler)                #['string', '�rnek']:>> is istance, hatırlamıyorsan OOP 1. videoyu izle , bu bir nesne ve bir clas alıyordu, nesne clastan ise true değerini döndürüyordu
# true- false'yi listelemek isteseydim "isinstance" yerine "bool" yazardım. o benim için bool değerlerini seçerdi.

# 8- Aşağıdaki sözlük veri yapısına sahip listede, adı "a" ile başkayan elemanları filtrel
liste = [{"Ad":"Ahmet","Yaş":20},{"Ad":"Banu","Yaş":22},{"Ad":"Can","Yaş":18},{"Ad":"Anıl","Yaş":28}]
a_ile_baslayanlar = list(filter(lambda kisi: kisi["Ad"].startswith("A"),liste))    # bu kişinin ad a ile başlıyor mu
print(a_ile_baslayanlar)        #[{'Ad': 'Ahmet', 'Ya�': 20}, {'Ad': 'An�l', 'Ya�': 28}]

# 9- Yukarıdaki listedeki yaşı 20 den büyük olanları al.
yirmiden_buyuk = list(filter(lambda kisi: kisi["Yaş"] > 20, liste))
print(yirmiden_buyuk)           #[{'Ad': 'Banu', 'Ya�': 22}, {'Ad': 'An�l', 'Ya�': 28}]
# map'a oldukça benziyor gördüğünüz gibi.
