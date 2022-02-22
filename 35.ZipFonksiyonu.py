# zip fonksiyonu
# en son map filter ve reduce fonk. işlemiştik. zip fonk. da onlar gibi phyton'da gömülü halde bulunmaktadır.
# oldukça kolay ve anlaşılabilir bir fonk.
# ne yapar? zip, fermuar anlamına gelir. bir fermuarı kapatırken karşılıklı dişlilerin birbiri ile eşleşmesi gibi temel anlamda 2 adet listenin elemanlarını
# birbirleri ile eşleştiriyor
# nasıl eşleştiriyor? ilk elemanları,2. elemanları, 3.elemanları..
# bu sonucu istediğimiz formata çevirebiliyoruz
liste1 = [1,2,3,4]
liste2 = ["a","b","c","d"]
liste3 = zip(liste1,liste2)
print(liste3)           #<zip object at 0x0000000F350602C0>: yazdırmak için bunu önce listeye çevirmeliyiz.
liste3 = list(zip(liste1,liste2))
print(liste3)           #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# yerlerini değiştirirsem ne olur?
liste3 = list(zip(liste2,liste1))
print(liste3)           #[('a', 1), ('b', 2), ('c', 3), ('d', 4)]: yani burada parametreleri gönderme sıranızın bir önemi var, ilk srıaya yazdığınız parametre çıktıda da ilk sırada olur

# bunları set olarak yazdıralım.
liste3 = set(zip(liste2,liste1))
print(liste3)           #{('a', 1), ('d', 4), ('c', 3), ('b', 2)}

# bir iki tane inceliğe değinelim
# bu fonksiyonu 2 taneden daha fazla liste ile de kullanabiliriz.
liste4 = list("pyton")
liste5 = [1,2,3,4]
liste6 = ["A","B","C"]
liste7 = list(zip(liste4,liste5,liste6))
print(liste7)           #[('p', 1, 'A'), ('y', 2, 'B'), ('t', 3, 'C')]: liste 6'nın elemanları bittiğinde zip fonksiyonunun işi bitti.
# yani eleman sayısı en az olan listenin elemanları bittiğinde zip fonk. biter

# zip fonk. ile her nesneyi kullanabilirsiniz, demet, küme, liste...
# elemanları sırayla birleştirip bize bir iterator döndürüyor.
# bir sonraki dersimizde sizlere değişkenlerin kapsama alanlarından ve scop kavramlarından bahsedicem. sonrasında iterator ve generator ile yolumuza devam edeceğiz.
