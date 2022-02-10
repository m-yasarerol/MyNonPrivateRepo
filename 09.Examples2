# KENDİME NOT: BU KISIMDAKİ ÖRNEKLERİ ANLAMAKTA ZORLANIYORUM.
#Öğrendiklerimizi örneklerle pekiştireceğiz.
# buradaki örnekler biraz daha karmaşık.

# ilk 10.000 asal sayının kaç tanesi 3 ile başlar 7 ile biter?
# bunu yapmak için ilk önce bir liste oluşturup o listeye asal sayıları sırayla eklicem. o listenin eleman sayısı 10.000 olduğunda durucam
# onrasında 3 ile başlayıp 7 ile biten sayıları bir listeye alıcam

from asyncio import start_server


prime_list = list()     #boş liste oluşturdum
prime_list.append(2)    
sayi = 3                #3 ten itibaren tüm sayıları asal mı değil mi diye kontrol edicem

while True:
    prime = True        # yani ele aldığım bir sayıya asal sayı muamelesi yapıcam, herhangi bir sayya bölündüğünde asal değildir dicem.
    for i in range(2,int(sayi ** 0.5) + 1):
        if sayi %i == 0:        # sayının i ye bölümünden kalan 0 ise..
            prime = False       # asal değil dedim
            break               # diğer sayılara bakmasına gerek yok
    if prime:                   # sayım asal sayı ise for döngüsündeki if bloğuna hiç girmeyecek
        prime_list.append(sayi) # asal sayıyı listem ekledim.
        if len(prime_list) == 10000:
            break               # listenin elemanı 10.000 olduğunda bitir.
    sayi += 1                   # bunu yazmazsan listeye hep 3 eklersin
# şimdi bu sayların kaç tanesi 3 ile başlayıp 7 ile bitiyor ona bakıcam
liste2 = []                     # boş bir liste daha oluşturdum ki 3 ile başlayıp 7 ile biten değişkenleri ekleyebileyim.
for prime in prime_list:
    strprime = str(prime)       # string foksiyonu kullanacağım için değeri stringe çevirdim
    if strprime.startswith("3") and strprime.endswith("7"): #Hatrla, ilk ders işlediğimiz metot. bunu biliyorsun
        liste2.append(prime)    # bu döngü tamamlandığında 3 ile başlayıp 7 

print(liste2)
print(len(liste2))

# aslında kodumuz çalışıyor, ancak çok ağır bir kod oldu, yavaş çalışıyor. Bunu optimize etmemiz gerekiyor.
# 17 . satırdaki kodu optimize ettim.

# problem 2: 3 basamaklı sayıların kaç tanesi rakamların küplerinin toplamına eşittir?
liste3 = []
for sayi in range(100,1000):
    toplam = 0
    gecici_sayi = sayi          # bir geçici sayı değikeni oluşturdum ve kendisine ilk deneyeceğim sayıyı atadım.
    while gecici_sayi != 0:     # tüm basamakları bu şekilde aldım
        basamak = gecici_sayi % 10
        toplam += basamak ** 3
        gecici_sayi //= 10
    if toplam == sayi:
        liste3.append(sayi)
print(liste3)

# problemm 3: fibonacci sayı dizisi ilk iki terimi 1 olan ve sonraki her terimi kendisinden önce gelen 2 terimin toplamı olan bir sayı dizisidir. ilk 100 fibonecci sayısını ekrana yazdırın.
#1,1,2,3,4,8,13,21...
fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)

index = 2
while True:
    fibonacci_list.append(fibonacci_list[index - 2] + fibonacci_list[index - 1])    # fibonacci listesine 0. ve 1. indexi ekledim
    index += 1                      # bir soraki adımda indexin 3 olması gerekiyor. bendde bu sayede 1 ve 3. indexi eklemeliyim.
    if len(fibonacci_list) == 100:  
        break                       # eleman sayısı 100 olduğunda döngüden çık
print(fibonacci_list)

# bir de for döngüsü ile yapalım
fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)

for i in range(2,100):
    fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])
print(fibonacci_list)

# problem 4: 100 basamaklı ilk fibonacci sayısını ekrana yazdırın.
fibonacci_list2 = []
fibonacci_list.append(1)
fibonacci_list.append(2)

index = 2
while True:
    fibonacci_list.append(fibonacci_list[index - 2 ] + fibonacci_list[index - 1])
    terim = fibonacci_list[index - 2 ] + fibonacci_list[index - 1]  # eklediğim 2 terimi aldım
    if len(str(terim)) == 100:
        print(terim)
        break
    index += 1

# bir önceki problemlere göre biraz daha karışıktı. 
