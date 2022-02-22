# local, enclosing, global, built-in varitables
# scope: bir değişkenin kullanılabilir olduğu aralıkları inceleyeceğiz. buradan yola çıkıp yerel ve global değişkenlere, başka ne tip değişkenler var
# onları inceleyeğiz. bunları inceleyip kullanımlarına değineceğiz.

# temel kural: bir değişkeni kullanmadan önce tanımlamak zorundasın
# kullanım 1
x = 5
print

# kullanım 2 
print(y)    #error!
y = 6   

# kullanım 3
def fonk():
    print(c)
c = 5 
fonk()      #5

# kullanım
def fonk():
    print(c)
fonk()      #error! : fonksiyonu çağırmadan önce tanımlamak zorundasın.    
c = 5 

# global ve local(yerel) değişkenler
b = "global x"      #>> bu bir global değişkendir. çünkü programın en seviyesinde tanımlandı, ve bu programın her yerinden erişilebilir(tanımlandıktan sonra) bir değişken
# local değişkenler: onlar da bir fonksiyonun içinde tanımlanan, ve sadece tanımlandığı fonksiyonda/döngüde geçerli olan değişkenlerdir. 
def fonk():
    y = "local y"
    print(y)
fonk()      #local y       
print(b)    #global x
print(y)    # error: y tanımlı değildir. çünkü buradaki y bir local değişkendir, bir fonksiyonun içinde tanımlanmıştır. buna dışarıdan ulaşamayız. sadece tanımlı olduğu fonksiyonun içinde kullanılabilir. işte buna local değişken denir.

x = "global x"
def fonk():
    x = "local x"
    print(x)

fonk()      # local x
print(x)    # global x: araya fonksiyon girmesi, değişkeni değiştirmedi. iki farklı değişken gibi davrandılar.

# enclosing ne demek? : iç içe fonksiyonlar var ise, en içteki local, bir üstündeki enclusing, en dışarıdaki global olur.
x = "global x"
def outer():
    x = "enclosing x"
    print(x)
    def inner():
        x = "local x"
        print(x)
    inner()

outer()     # enclosing x
            # local x
print(x)    # global x


x = "global x"
def fonk():
    x = 5
fonk()
print(x)    # global x: 2 x aynı değildir.

# fonksiyonun içinden global değişkeni değiştirmek istersem ne yapacağım?
x = "global x"
def fonk():
    global x
    x = 5
fonk()
print(x)    # 5: phyton' a local bir x değil, var olan global x değerini kullanmak istiyorum dedim.
# eğer ben bir fonksiyonun içerisinden yani daha içteki bir scoptan global değişkeni kullanıp onu değiştirmek istiyorsam, "global" anahtar kelimesinden faydalanacağım.

# iç içe fonksiyon varsa ben enclosing variable yani ortadaki değişkeni de kullanabilirim. nasıl?
x = "global x"
def outer():
    x = "enlosing x"
    print(x)
    def inner():
        x = 5
    inner()
    print(x)    # içerideki scopa bakmadı, bir üst scopa baktı.
outer()     # enlosing x
            # enlosing x
# enlosing değişkeni değiştirelim
x = "global x"
def outer():
    x = "enlosing x"
    print(x)
    def inner():
        nonlocal x  # bir önceki basamakta kullanılan x değerini kullanacağımı ifade ediyorum.
        x = 5
    inner()
    print(x)    
outer()     # enlosing x
            # 5

# build- in : özel isimler, phytonda kullanmaktan çekinmemiz gereken isimler.
# örnek: sum, max, len, lambda: yani bunlar phytonda bir anlamı olan kelimeler, bunları değişken ismi olarak kullanırsanız, mesela siz "sum" isimli bir fonksiyon oluşturursanız
# phytonda var olan fonksiyonunu overrated etmiş olursunuz. o nedenle önerilmez. illa ki kullanmanız gerekiyorsa sonuna alt çizgi ekleyerek kullanın "sum_"
# o nedenle çok özel durumlar dışında phytonda var olan fonksiyonları değişken olarak kullanmamalıyız.
# değişkenlerin nasıl tanımlandıkları, nasıl geçerli olduklarına değindik.
# overrated: abartmak, gereğinden fazla kullanmak.
