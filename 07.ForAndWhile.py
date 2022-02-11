# listeler ile for döngüsü
# range fonksiyonu ile for döngüsü
# iç içe for döngüleri
# break ve continue anahtar kelimeleri
# while döngüsü
# önemli bir konu
# nedir?: bir listenin elemanlarını yazdırmak istediğimizde her biri için print kullanmak yerine döngü kullanırız.
# yani listenin her bir elemanına aynı işlemi yapar.

liste = [1,2,3,4]
print(liste[0])                 #1
print(liste[1])                 #2
print(liste[2])                 #3
print(liste[3])                 #4
#yerine
liste = [1,2,3,4]
for rakam in liste: #rakam listenin için olduğu sürece bana bu rakamı yazdır.
    print(rakam)                #1
                                #2
                                #3
                                #4

isim = "Ahmet"
for harf in isim:
    print(harf)                 #A
                                # h
                                # m
                                # e
                                # t  
# for döngüsü listelerde , demetlerde  strginlerde kullanabilirsin.
# range fonksiyonu belirlediğiniz iki sayı arasındaki değerleri verir: ilk snırı dahil eder, ikinci sınırı dahil etmez.
for i in range(0,10):
    print(i)                    # 0
                                # 1
                                # 2
                                # 3
                                # 4
                                # 5
                                # 6
                                # 7
                                # 8
                                # 9
for i in range(1,17,2):
    print(i)                    # 1
                                # 3
                                # 5
                                # 7
                                # 9
                                # 11
                                # 13
                                # 15
# yukarıdaki kodda:
#> ilk parametre başlangıç değerimiz.
#> ikinci parametler bitiş değerimiz.
#> aralık (ikişer ikişer)
#herhangi bir işlemi bu şekilde tekrarlatabiliriz.

#rangenin içine tek bir değer yazarsan, başlangıcı kendisi sıfır olarak alır. yani
for i in range(10): = for i in range(0,10):

#ekrana 2^10 yazdırmaya çalışalım
sonuc = 1
for i in range(10):
    sonuc *= 2

print(sonuc)                    #1024
# yani sonucumuz 10 kez 2 ile çarpııldı ve yazdırıldı.
#range fonksiyonu bir ilşemi belirli bir sayıda tekrarlamak için kullanılır.

liste1 = ["a", "b", "c"]
liste2 = [1,2,3]
for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)       # a 1
                                # a 2
                                # a 3
                                # b 1
                                # b 2
                                # b 3
                                # c 1
                                # c 2
                                # c 3
# bu şekilde for döngülerini iç içe kullanabiliriz.

#break ve cuntinue anahtar kelimeleri
#3 ü yazdıemasını istemiyorum.
#continue: alltakileri atla ve devam et anlamına gelir. Döngüyü sonlandırmaz, belirli bir koşulda döngünün bir sonraki adımına geçmeyi sağlar.
#continue yerine break kullansaydım 3'ü atladık yazıp döngüyü sonlandırırdı.
# break döngüyü sonlandırır, continue bir elemanı pas geçmeyi sağlar.
liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if i ==3:
        print("3'ü atladık.")
        continue
    print(i)                    # 1
                                # 2
                                # 3'� atlad�k.
                                # 4
                                # 5
                                # 6
                                # 7
                                # 8
                                # 9

# 99 ' kadar sadece 3'e bölünebilen sayılar.

liste = range(99)

for i in liste:
    if i % 3 != 0:
        continue
    if i == 81:
        break
    print(i)
# i 81 olduğu anda döngüden çıktı.

#while döngüsü: belirli bir koşul sağlandığı sürece çalışan bir döngüdür.
x = 2
while x < 10:
    print(x)
    x += 1                      # 2
                                # 3
                                # 4
                                # 5
                                # 6
                                # 7
                                # 8
                                # 9
# kod şu şekilde çalıştı:
# iki ondan küçük olduğu için yazdırdı, bir ekledi.
# üç ondan küçük olduğu için yazdırdı, bir ekledi.
# dört ondan küçük olduğu için yazdırdı, bir ekledi ve böyle devam etti.
# x = 10 olduğunda koşul bozuldu.

x = 2
y = 3

while x * y < 1000:
    print(x,y)
    x += 2
    y +=2

#bunların çarpımı bin ve binden küçük oldukça çalışmaya devam etti.

# bir de whilenin değişik bir özelliği daha var, bazen sadece bir koşul sağlandığında döngüdeç çıkmak istersiniz.
i = 1
while True:
    print(i)
    i += 1
# kod sen durdurana kadar çalışmaya devam eder.
while True:
    print(i)
    i += 1
    if i == 10000:
        break
#10.000 olduğunda döngüyü bitirir.

# 1000'e kadar olan tek sayıları yazdırmaya çalışalım.
i = 1
while True:
    if i %2 == 0:
        i += 1      # burayı atlarsan programın çıktısı sadece 1 olur. Döngü durmadan başa dönmeye devam eder.
        continue
    print(i)
    i += 1          #burayı atlarsan program durmadan 1 yazmaya devam eder.
    if i == 1000:
        break
#2'ye bölünen sayıları atladım. ve i ye 1 ekleyerek döngüye devam ettim. ta ki 1000 olana kadar.
# dolayısıyla while döngüsünü sonsuz olarak kullanıyorsan, değişkeninizi bir yerlerde arttırmayı unutmayın yoksa döngü kısır döngüye girebilir.
# bundan sonraki bir kaç video alıştırma olacak.
