# fonksiyonlara parametre olarak fonksiyon göndermek.
# fonksiyonların ileri düzey özelliklerini inceliyoruz: 
# kabaca şöyle bir yol izledik,
# >>iç içe fonksiyonların kullanımını öğrendik
# >> fonksiyonlardan fonk. geri döndürmeyi öğrendik( return ile )
# >> bu gün de fonksiyonlara parametre olarak fonk. göndermeyi öğrenip decoratore geçeceğiz.
def topla(x,y):
    return x + y
def carpma(x,y):
    return x * y

def islem_yap(fonk,a,b):        # ben buradan fonksiyonu ve 2 sayı gircem, bu fonk. yapcağı şey, benim girdiğim sayıları benim girdiğim fonksiyona koyup bana sonucunu söylemek olacak
    return fonk(a,b)

print(islem_yap(topla,3,5))     #8
print(islem_yap(carpma,3,5))    #15
# bu şekilde fonksiyonları da diğer fonksiyonlara parametre olarak gönderebilirsiniz, ancak dikkat edeceğiniz nokta şu, fonksiyonu gönderirken fonk. sadece ismini göndereceksin, parantezlerini değil.

# şimdi güzel bir örnek yapalım
# liste = [1,2,3,4,5,6,7,8]
# fonk = x * x 
# sonuc = [1,2,9,16,25,36,49,64]
# yani bir fonk yazıcam, ona bir liste ve fonk vericem, verdiğim listedeki tüm elemanları ffonksiyonlardan yerine koyacak ve sonuçlardan bir liste oluşturacağız
# bunu phytonda "map" fonk. zaten yapıyor. ama kendimiz yapacağız
liste1 = [1,2,3,4,5]
liste2 = [1,3,4,5,8,9,11]
def kare_al(x):
    return x * x
def kup_al(x):
    return x ** 3

def map_fonk(fonk,liste):       # parametre ile gelen listedeki tüm elemanları fonk. koyacak, fonk'dan gelen elemanları da sonuç listesine ekleyecek
    sonuc = []
    for i in liste:
        sonuc.append(fonk(i))
    return sonuc

print(map_fonk(kare_al,liste1)) #[1, 4, 9, 16, 25]>> liste1 'in karesini aldı
print(map_fonk(kup_al,liste2))  #[1, 27, 64, 125, 512, 729, 1331]>>Ç liste2'nin küpünü aldı.
# diyelim ki söz 10 sınıfa giriyorsunuz, her sınıfta 50 öğrenci var, her sınıfın ortalaması için ayrı ayrı fonk. yazmana gerek kalmaz. sadece liste ismi değiştirmen yeterli.
# bunlar iyi öğrenin çünkü bunları bilmeden decorator kavramını öğrenmeniz mümkün değil.
