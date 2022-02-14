# nedir? elimizde bir tane liste olacak, biz bu listeden yola çıkarak belirli kurallara göre yeni listeler oluşturacağız.
# örnekleri önce öceden öğrendiğimiz şekilde, sonrasında list comprehension ile çözeceğiz. aradaki kolaylık farkını görmeniz adına

# örnek 1: verilen listedeki rakamlardan oluşan bir liste oluşturalım
numbers = [1,2,3,4,5,6,7,8,9]
# mevcut bilgimizle nasıl yapabiliriz?
list2 = []
for number in numbers:
    list2.append(number)
print(list2)
# list comprehension ile:
list3 = [number for number in numbers] 
print(list3)
# ilk kısım listeye eklenecek olan eleman, sonraki kısım bu elemanın nerede bulunduğunu ifade eder. yukarıdaki 4 satır kod yerine tek satırda yazdım.

# örnek 2: listedeki rakamların karelerinden oluşan bir liste oluşturalım
numbers = [1,2,3,4,5,6,7,8,9]
# mevcut bilgimiz ile:
list2 = []
for number in numbers:
    list2.append(number*number)
print(list2)
# list comprehension ile:
list3 = [number*number for number in numbers]
print(list3)
# format: listeye neyi ekleyeceğim-nerede?

# örnek 3: verilen listedeki çift rakamlardan bir liste oluşturalım
numbers = [1,2,3,4,5,6,7,8,9]
# mevcut bilgimiz ile:
list2 = list()
for number in numbers:
    if number %2 == 0:
        list2.append(number)
print(list2)
# list comprehension ile: koşul en sona yazılır
list3 = [number for number in numbers if number %2 == 0]
print(list3)
# sıralama: en başa eklenecek eleman, sonra o elemanın bulunduğu liste/küme, elemanın sağlaması gereken koşul

# örnek4: verilen listedeki çift rakamların karelerinden oluşan bir liste oluşturalım
numbers = [1,2,3,4,5,6,7,8,9]
# mevcut bilgimiz ile:
list2 = list()
for number in numbers:
    if number %2 == 0:
        list2.append(number*number)
print(list2)
# list comprehension ile:
list3 = [number *number for number in numbers if number %2 == 0]
print(list3)

# örnek 5: verilen listedeki 4'ten büyük çift sayıların karelerinden oluşan bir liste oluşturalım
numbers = [1,2,3,4,5,6,7,8,9]
# mevcut bilgimiz ile:
list2 = []
for number in numbers:
    if number > 4 and number %2 == 0:
        list2.append(number ** 2)
print(list2)
# list comprehension ile:
list3 = [number * number for number in numbers if number > 4 and number %2 == 0]
print(list3)

# örnek 6: 
numbers = [1,2,3,4]
letters = "abcd"
# [(1,a),(1,b),(1,c),(1,d),(2,a),...,(4,d)] biçimimfr ikililerden oluşan bir liste oluşturalım
# mevcut bilgimiz ile:
list2 = []
for number in numbers:
    for letter in letters:
        list2.append((number,letter))
print(list2)
# list comprehension ile:
list3 = [(number,letter) for number in numbers for letter in letters]
print(list3)
# demet olduğu için paranteze aldım
# sıralamalar birbirine çık benziyor

# örnek 7:
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,6,9,5]
# birinci listede bulunup ikinci listede bulunmayan rakamların karesinden oluşan bir liste yapalım
# mevcut bilgimiz ile:
list3 = []
for i in list1:
    for i not in list2:                     # syntax hatası aldım, nedenini bilmiyorum.
        list3.append(i * i)
print(list3)
# list comprehension ile:
list4 = [i*i for i in list1 if not i in list2]
print(list4)

# örnek 8:
list_ = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
# verilen listedeki elemanları tek tek alan [1,2,3,4,5,6,7,8,9,10,11,12] biçiminde bir liste oluşturalım
# mevcut bilgimiz ile:
list2 = []
for i in list_:
    for j in i:
        list2.append(j)
print(list2)
# list comprehension ile:
list3 = [j for i in list_ for j in i]       # önce i'li listenin elemanı olarak tanımladım, sonra j yi i nin elemanı olarak tanımladım
print(list3)

# listelerin metotlarını listelediğimiz bir program yapmıştık. alt çizgi ile başlayan metotları filtrelemek için şöyle bir kod yazmıştık
list_methods = []
print(dir(list))
for method in dir(list):
    if method.startswith("__"):
        continue
    list_methods.append(method)
print(list_methods)
# o kodu list comprehension ile yazalım
liste = [method for method in dir(list) if not method.startswith("__")]  # method eklenecek, dir(list)'in içinde bulunacak, __ ile başlamayacak
print(liste)

# önemli bir dersti, önceden yazdığımız bazı kodları nasıl daha kısa yazacağımızı öğrendik.
