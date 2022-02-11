# şimdi önemli modülleri teker teker incelemeye çalışacağız
# random, uniform modülü
# randint ve randrange fonksiyonları
# choice, shuffle ve sample fonkisyonları

# random modülü: bizim için rastgele sayılar veya değerler üreten fonksiyonları barındırır. görelim:
# herhangi bir modüldeki tüm fonkisyonları öğrenmen mümkün değil , en çok kullanılanları inceleyeceğiz. spesifik bir fonksiyona ihtiyaç duyarsan o modülün dökümantasyonunu okursun.
# ctrl+ yapar ve modülün ismine tıklarsan o modüle gider, oradaki fonkisyonları inceleyebilirsin.
# ilk inceleyeceğimiz fonksiyon random ve uniform fonk.
import random

for i in range(10):
    print(random.random())          # random modülünün içinde random fonkisyonu var.
# random fonkisyonu bize sıfır ile 1 aralığında rastgele ondalık sayılar üretiyor.
print(range)
# her çalıştırdığımda farkklı bir on sayı gelece. 

# peki 0-1 aralığında depil de kendi ürettiğin aralıkta rastgele ondalık sayı üretmek istersen hangi fonksiyonu kullanacaksın?
# uniform fonksiyonu: bir alt sınıf ve üst sınır ister
for a in range(10):
    print(random.uniform(10,20))    #>19.83007959464627
                                    # 12.78495468431211
                                    # 18.930430579662495
                                    # 11.349867596952555
                                    # 16.389341637783836
                                    # 15.865799106879074
                                    # 14.917447855988094
                                    # 16.561687486380315
                                    # 14.183342831891064
                                    # 18.767448618307576
# random fonkisyonu 0-1 aralıkta sayılar üretirken, uniform fonkisyonu bizim belirlediğim aralıkta sayılar üretir.

# tam sayılar nasıl üreteceğiz? 
# randint ve randrange fonkisyonlarını kullanacağız.
# randint fonksiyonu da alt sınır ve üst sınır bekler, ama dikkat et! her iki sınırı da dahil etti.
import random
for c in range(10):
    print(random.randint(1,5))      # 1
                                    # 1
                                    # 3
                                    # 3
                                    # 5
                                    # 5
                                    # 5
                                    # 1
                                    # 1
                                    # 4 >> gördüğün gibi 5 ' i de dahil etti.
#randrange nedir? : o kadar kullanmazsınız ama, 3 parametre alır, kaçar kaçar artan sayılardan seçeceğini de belirtebilirsin. üst sınır dahil değil. üst sınırın dahil olması sadece randint de var
# görelim:
import random
for i in range(10):
    print(random.randrange(1,10,2)) # 9
                                    # 3
                                    # 7
                                    # 3
                                    # 1
                                    # 5
                                    # 5
                                    # 3
                                    # 1
                                    # 1>>2 şer 2 şer artan sayılardan seçti, üst sınırı dahil etmedi.
# belirlediğin bir aralıkta, belirli bir miktarda artan sayılardan size değer döndürür. 2 parametreyle kullanırsan randintten çok farkı kalmaz

# bunlar sayı üretmek için kullandığım fonkisyonlardı, bir de listeler ile ilgili fonkisyonlarımız var
import random
liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]
print(random.choice(liste))                                   
#choice, verdiğin listeden rastgele bir eleman seçer
 
#shuffle : bize bir sonuc üretmez, listemizdeki elemanların yerlerini değiştirir.
import random
liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]
random.shuffle(liste)
print(liste)                        # ['Gri', 'Mavi', 'Ye�il', 'Beyaz', 'Siyah', 'Turuncu']
# shuffle zaten ingilizce de karıştır demek.

#sample: örnekle gibi bir anlamı var. Parametre olarak bir liste ve eleman sayısı alır, verdiğin listeden istediğin kadar eleman çeker
import random
liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]
print(random.sample(liste,3))       #['Turuncu', 'Mavi', 'Siyah']

# bunlar random modülünün fonkisyonları idi. şimdi 2 adet programa bakacağız.

# bir zar attığımızda 6 gelme olasılığını hesaplayan program
import random 
zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,}  # sözlüğümü oluşturdum
for i in range(100):                # zarımı 100 kere attırıcam
    zar = random.randint(1,6)       # 1-6 arrasında sayılar üretir
    zarlar[zar] += 1                # zar sözlüğüne eklicek

for zar in zarlar:
    print(f"{zar} gelme olasığı: {zarlar[zar] / 100}")  # 1 gelme olas���: 0.18
                                                        # 2 gelme olas���: 0.14
                                                        # 3 gelme olas���: 0.22
                                                        # 4 gelme olas���: 0.11
                                                        # 5 gelme olas���: 0.1
                                                        # 6 gelme olas���: 0.25

# tavla oynarken 6-6 kıymetli bir zardır. 10 kere 6-6- gelmesi için kaç kez zar atmanız gerekir.
import random
alti_alti = 1
deneme_sayiyi = 0               # kaç kez zar attığımızı gösterir
while True:                     # "benim belirlediğim bir koşul gerçekleşene kadar denemeye devam et"
    deneme_sayiyi += 1          #bir zar attım
    zar1 = random.randint(1,6)  # rastgele 1-6 arasında sayı üret
    zar2 = random.randint(1,6)
    if zar1 == 6 and zar2 == 6:
        alti_alti += 1          # iki zar da 6 geldiğinde alti_alti değişkenine 1 ekle
    if alti_alti == 10:
        print(f"10 kere  6-6 gelmesi için zarlar {deneme_sayiyi} kadar atıldı.")
        break                   #döngüyü bitirmeyi unutma
                                #output: 10 kere  6-6 gelmesi i�in zarlar 405 kadar at�ld�
# faydalı bir modüldür. çekişil ile ya da rastgele değerler içeren herhangi bir fonkisyona ihtiyaç duyarsan yolun random modülü ile kesişecek.
# sık kullanılan fonksiyonlara değinmeye çalıştım.
