# map fonksiyonu kullanımı
# oldukça kullanışlı, yazdığımız kodun daha kısa ve anlaşılır olmasını sağlıyor.
# bizden parametre olarak bir fonk. ve bir liste alyor, sonra listedeki elemanları teker teker fonksiyonda yerine koyuyor, ve elde ettiği sonuçlardan yeni bir liste üretiyor
# yani kabaca bir listedeki elemanların hepsine aynı işlemi yapıyor diyebiliriz
liste = [1,2,4,5,7]
def kare_al(x):
    return x * x
# şimdi istediğimiz şu, listedeki elemanların hepsini bu fonksiyona gönderip, oradan gelen sonuçlar ile başka bir liste oluşturacağız.

# bunu önceden şöyle yapıyorduk:
liste2 = []
for i in liste:
    liste2.append(kare_al(i))
print(liste2)                   #[1, 4, 16, 25, 49]

# şimdi "map" ile yapacağız:
liste3 = map(kare_al,liste)     # benden parametre olarak bir fonksiyon ve bir liste istedi.
print(liste3)                   #<map object at 0x000000B80E3E1FA0>: map objesidir dedi. bunun kendine has bir tipi var. bize özel bir map objesi olarak dönüyor. çünkü bunu siz sonradan istediğiniz formata çeviriyorsunuz (liste,küme,demet..)

# listeye çevirelim:
liste3 = list(map(kare_al,liste))

# kümeye çevirelim:
liste3 = set(map(kare_al,liste))

# demete çevirelim:
liste3 = tuple(map(kare_al,liste))

# biraz daha ilerleyelim. hatırlarsanız lambda konusunu işlerken lambda'nın map, reduce ve filter fonk. ile çok güzel kullanıldığınız söylemiştim
liste = [1,2,3,6,7,9]
liste4 = list(map(lambda x : x * x , liste))
print(liste4)                   #[1, 4, 9, 36, 49, 81]>> fonksiyonu tek satırda yazdık.

liste5 = list(map(lambda x : x ** 3,liste))
print(liste5)                   #[1, 8, 27, 216, 343, 729]>> küplerden oluşan bir liste yaptık.
# yani listedeki elemanların hepsine aynı işlemi uygulamak istiyorsanız map fonk. faydalanmak çok akıllıca.

# biraz daha ilerleyelim, iki tane liste ile kullanalım. bir fonk. olsun ve 2 adet liste olsun
liste6 = [1,2,4,7,8]
liste7 = [3,5,9,0,1]
# bu elemanların, aynı sırada olanların toplamlarından oluşan bir liste istiyorum. 
def toplam(x,y):
    return x + y
sonuc = list(map(toplam,liste6,liste7))
print(sonuc)                    #[4, 7, 13, 7, 9]
#yukarıdaki örnekte 3 adet liste olsaydı sonuca 3 adet liste ismi veririm. görelim, ama 3. liste 3 elemanlı olsun.
liste8 = [1,2,4,7,8]
liste9 = [3,5,9,0,1]
liste10 = [2,5,10]
def toplam(x,y,z):
    return x + y + z
sonuc = list(map(toplam,liste8,liste9,liste10))
print(sonuc)                    #[6, 12, 23]>> bir sorun olmadı. liste10 daki elemanlar bittiğinde fonksiyonumuz durdu.

# aynı sonucu lambda ile de ifade edelim:
sonuc2 = list(map(lambda x,y,z: x + y + z,liste8,liste9,liste10))
print(sonuc2)                   #[6, 12, 23]>> herhangi bir fark olmadı, kodum kısaldı.
# dolayısı ile map fonksiyonuna birden fazla liste gönderebiliriz ancak kaç tane liste gönderiyorsak fonksiyonumuzun da o kadar parametre alması gerekiyor.

# başka bir örnek yapalım
urunler = [["Ayakkabı",150],["Pantolon",120],["Gömlek",100],["Ceket",200]]
# bizim böyle bir ürünler listemiz var. diyelim ki biz bunların hepsine %10 indirim yapmak istiyoruz.
def indirim_yap(x):
    urun,fiyat = x[0],x[1]
    fiyat = fiyat * (9 / 10)
    return [urun,fiyat]

sonuc = list(map(indirim_yap,urunler))
print(sonuc)                    #[['Ayakkab�', 135.0], ['Pantolon', 108.0], ['G�mlek', 90.0], ['Ceket', 180.0]]

# başka bir örnek daha yapalım
isimler = ["AhMeT","aYşE","HÜseyN"]
# diyelim ki bir e-ticaret sitesinde çalışıyoruz. bize gelen isim listesi istediğimiz formatta değil. bu isimlerin tüm harfini küçük yazdırmak istiyoruz.
isimler2 = list(map(lambda x : x.lower(),isimler))
print(isimler2)                 #['ahmet', 'ay�e', 'h�seyn']>> fonksiyonu parametre olarak gönderdiğimizde parantezi kullanmıyorduk. ancak burada bu parantez olacak, çünkü burada fonksiyonu çalıştırıp döndürdük. 
# burada parametre olarak x'i alıyor. lower'i çalıştırıp döndürüyor.
# baş harflerini büyük yapalım
isimler3 = list(map(lambda x : x.capitalize(),isimler))
print(isimler3)                 #['Ahmet', 'Ay�e', 'H�seyn']
