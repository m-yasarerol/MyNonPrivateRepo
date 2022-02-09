# # import rlcompleter
# # if ile kullanılabilecek oparatörler
# # eşittir '==', eğit değildir '!=', büyüktür '>', küçüktür '<', büyük veya eşittir '>=', küçük veya eşittir '<='
# # in anahtar kelimesi
# # not anahtar kelimesi
# # and ve or bağlaçları
# # is anahtar kelimesi (hafızada aynı nesne olmalı)
# # ne işe yarar: if yapısı belirlediğimiz bir koşulun gerçekleşmedi ya da gerçekleşmemesi durumunda belirli kodlar çalıştırmaya yarar.
# ^yani programda önce bir kontrol gerçekleştirir, o kontrolün sonucunda belirli kodlar çalıştırır

if True:
    print("koşul doğru")
    print("hala koşulun içindeyiz")     #ko�ul do�ru
                                        #hala ko�ulun i�indeyiz >> koşul doğru olduğun için ilk bloğu yazdı.
# true false kızımları dinamik olarak değişecek

a = 5
b = 7
if a == b:
    print("a = b")                      #false oldğu için değer döndürmedi.
a = 5
b = 5
if a == b:
    print("a = b")                      #a = b >> koşul doğru olduğu için çalıştı.

a = 18
b = 5
if a > b:
    print("a > b")                      # a > b

a = 18
b = 5
if a != b:
    print("a eşit değil b")             #a e�it de�il b >> "!=" eşit olmadığı anlamına gelir.

a = 5
b = 5
if a != b:
    print("a eşit değil b")             # çalışmadı. çünkü a b ye eşit ama biz değil dedik. (false)

# peki yanlış olma durumunda da bir değer döndürmek istiyor isek: "else" kullanacağız.

a = 6
b = 8
if a == b:
    print("a = b")
else:
    print("a != b")                     #a != b >> if koşulu gerçekleşmediği için else koşulu gerçekleşti.

# peki bunu biraz derinleştirmek istersek: [birkaç alt parçaya böleceğiz]
# elif = başka bir koşul ifade eder. "eğer öyle değil de böyle ise" yani bunun yanına da bir koşul gelecek.
# else = kendinden önceki if ifadeler çalışmasa sorgusuz sualsiz çalışır.

renk = "siyah"
if renk == "beyaz":
    print("beyaz")
elif renk == "sarı":
    print("sarı")
elif renk == "mavi":
    print("mavi")
else:
    print("hiçbiri")                    # hiçbiri

# yukarıda kodun algoritması şöyle çalışır:
    # > rengi kontrol ediyor . beyaz mı? renk beyazsa if bloğu çalışacak ve diğerlerini es geçecek. Çünkü alttaki koşullar diğerlerinin alternatifi.
    # > rengimiz sarı mı ? hayır. es geçip bir alt koşula bak.
    # > rengimiz mavi mi ? hayır. es geçip bir alt koşula bak.
    # > else tüm durumları kapsıyor. yani yukarıdaki koşulların hiçbiri çalışmadıysa else çalışacak.
# yani yukarıdaki kod parçalarından sadece ve sadece bir tanesi çalışacak.
# if'in altına istediğin kadar koşul ekleyebilirsin. unutma ama yanına bir koşul daha eklemek gerek.
# else yanına koşul almaz.

# and ve or bağlaçları
# if ile beraber kullanabiliriz.
# or anahtar kelimesi mantıksal bir bağlaçtır. doğru olması için iki ifadeden birisinin doğru olması yeterlidir.
a = 5 
b = 8
c = 10
if a < b  or c > a:
    print("koşul doğru")
else:
    print("koşul yanlış")               #ko�ul do�ru

a = 5 
b = 8
c = 10
if a < b  or c == a:
    print("koşul doğru")
else:
    print("koşul yanlış")               #ko�ul do�ru (koşullardan birisi doğru olsa da true çalıştırdı)

a = 5 
b = 8
c = 10
if a > b  or c == a:
    print("koşul doğru")
else:
    print("koşul yanlış")               #ko�ul yanlış (koşullardan ikisi de yanlış olduğundan false çalıştırdı)

a = 5 
b = 8
c = 10
if a > b  or c == a or b > a:
    print("koşul doğru")
else:
    print("koşul yanlış")               #ko�ul doğru (koşullardan birisi doğru olsa da true çalıştırdı. gördüğün gibi 3'lü bir yapı kullandım)

# bir de or'un kardeşi olan and bağlacı var. çalışması için bağladığı tüm ifadelerin doğru olmasıı gerekir.
a = 5 
b = 8
c = 10
if a < b  and b < c:
    print("koşul doğru")
else:
    print("koşul yanlış")               #ko�ul doğru (bağladığı tüm ifadeler doğru)

a = 5 
b = 8
c = 10
if a > b  or c < a:
    print("koşul doğru")
else:
    print("koşul yanlış")               #ko�ul yanlış (koşullardan birisi yanlış olduğundan false çalıştırdı)

# bunları kendi içinde de kullanabilirsin. (end ve or) ancak parantez kullanımına dikkat etmen gerekir. (temel düzey eğitim olduğundan eğitmen göstermedi)

# "in": içinde olup olmadığını kontrol etmeni sağlar
liste = [1,2,3,4,5,6,7,8,9]
a = 1
if a in liste:
    print("listede var")
else:
    print("listede yok")                #listede var

liste = [1,2,3,4,5,6,7,8,9]
a = 10
if a in liste:
    print("listede var")
else:
    print("listede yok")                #listede yok

liste = ["Phyton"]
a = "p"
if a in liste:
    print("listede var")
else:
    print("listede yok")                #listede yok (phyton için p != P)

liste = "Phyton"
a = "P"
if a in liste:
    print("listede var")
else:
    print("listede yok")                #listede var

# not anahtar kelimesi: var olan koşulu olumsuza çevirmeye yarar.
program = "Phyton"
a = "P"
if not a in program:
    print("Doğru")
else:
    print("Yanlış")                     #yanlış

a = 8
b = 10
if not a == b:
    print("koşul doğru")
else:
    print("koşul yanlış")               #koşul doğru

# is anahtar kelimesi: eşittire benziyor. is'in doğru olabilmesi için kıyasladığımız iki değişkenin özdeş yani hafızada aynı yerde olması gerkiyor.
a = "phyton"
b = "phyto"
b += "n"
print(a)
print(b)

if a == b:
    print("a = b")
else:
    print("a != b")                     # a = b

if a is b:
    print("a = b")
else:
    print("a != b")                     #a != b
# çünkü a bir değişken içinde phyton değişkeni var, b de başka bir değişken, onun içinde de phyton değeri var ama aslında bunlar aynı elemanlar değiş.
# hafızada bulundurdukları adrese bakalım:
a = "phyton"
b = "phyto"
b += "n"
if a is b:
    print("a = b")
else:
    print("a != b")
    print("a'nın ID'si:" + str(id(a)))
    print("b'nin ID'si:" + str(id(b)))   #a != b
                                        # a'n�n ID'si:1086552630960
                                        # b'nin ID'si:1086552932784
#bir sonraki dersimizde döngülere başlayacağız.
