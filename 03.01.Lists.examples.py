    ÇÖZERKEN ZORLANDIĞIM SORULAR: 9 VE 10. SORU
    
# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
markalar = "Bmw, Mercedes, Opel, Mazda".split()
print(markalar)

# 2- Liste Kaç elemanlıdır ?
markasayisi = len(markalar)
print(markasayisi)
# 4- Mazda değerini Toyota ile değiştirin.
markalar[-1] = "toyota"
print(markalar)

# 5- Mercedes listenin bir elemanı mıdır ?
kontrol = "Mercedes," in markalar
print(kontrol)

# 6- Listenin -2 indeksindeki değer nedir ?
a = markalar[-2]
print(a)
# 7- Listenin ilk 3 elemanını alın.
ilkuceleman = markalar[:3]
print(ilkuceleman)

# 8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
markalar[-2::] = ["toyota", "Renault"]
print(markalar)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
markalar2 = ["Audi", "Nissan"]
markalar.extend(markalar2)
print(markalar)

# 10- Listenin son elemanını silin.
del markalar[-1]
print(markalar)

# 11- Liste elemanlarını tersten yazdırınız.
markalar = "Bmw, Mercedes, Opel, Mazda".split()
markalar.reverse()
print(markalar)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

# # studentA: Yiğit Bilgi 2010, (70,60,70)
studentA = ["Yiğit", "Bilgi", 2010, [70,60,60]]
# # studentB: Sena Turan 1999, (80,80,70)
studentB = ["Sena", "Turan", 1999, [80,80,70]]
# # studentC: Ahmet Turan 1998, (80,70,90)
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.
print(studentA + studentB + studentC)

