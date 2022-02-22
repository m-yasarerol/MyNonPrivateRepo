# iterator, iterable ve iteration kavramları
# __iter__() ve __next__()
# bir döngü çalıştırıldığında, arka planda olup bitenlere göz atacağız. bu gün döngüler hakkında biraz daha derinlemesine bilgi sahibi olacağız
# sonrasında kendimiz bir class oluşturup ve oluşturduğumuz bu clasın nesnelerinin döngülerle nasıl kullanılabileceğini göreceğiz yani clasımız
# üzerinde nasıl bir iterator oluşturacağımızı göreceğiz. 
# eğer iteratorları iyi kavrarsak generator fonksiyonlarını daha kolay anlarsınız.
from tracemalloc import start
from turtle import end_fill


sayilar = [1,2,3]
for sayi in sayilar: 
    print(sayi)         # 1
                        # 2
                        # 3
# iteration, kelime anlamı olarak adımlama demektir. bir nesnenin elemanlarını teker teker ziyaret etme işlemine iteration deniyor.
# itreable ise, "üzerinde adımlama yapılabilen" anlamına gelir. yukarıda sayılar listesi, üzerinde adımlama yapılabildiğinden bir iterable nesnedir
# sadece listeler değil, döngüler ile kullanabileceğiniz tüm nesneler iterabledir.(string,demet, dosyalar..)
# iterator ise, az önce bahsettiğimiz adımlama işini yapan nesnedir, tüm elemanları teker teker gezer, nerede kaldığını da unutmaz.
# yukarıda sayılar listesine itareble dedik, peki tipini bilmediğimiz bir şeyin iterable olup olmadığını nasıl öğreneceğiz?
sayilar = [1,2,3]
print(dir(sayilar))     #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# yukarıdaki "dir", bize sayılar nesnesi ile kullanabileceğimiz metotları gösterir. yukarıda "__iter__" metodunu görüyoruz. iter metotdu, bir nesnenin 
# iterable olduğunu gösteriyor. eğer bir nesnenin içinde iter metodu var ise o iterabledir ve döngüler ile kullanılabilir. Peki bu iter ne yapıyor?
# __iter__ bir iterator geri döndürür.
i_sayilar = iter(sayilar)
print(dir(i_sayilar))   #......,'__next__',.......
# bit iterator'u iterator yapan bu next metodudur. bu bir sonraki elemana nasıl geçeceğini söyleyen metottur. yani next metodu çağrıldığında iterator
# bir sonraki elemana geçiyor diyebiliriz.
print(i_sayilar.__next__())     # 1
print(next(i_sayilar))          # 2
print(next(i_sayilar))          # 3
print(next(i_sayilar))          # eror: listede gitmediği başka eleman kalmadı.
# her çalıştırdığımda, nerede kaldıysa oradan devam ediyor. işte bu iterator'u iterator yapan şeydir. yani bir elemanı ziyaret ediyor, next 
# dediğinizde bir sonrakine gidiyor.
# işte döngüler bu şekilde çalışıyor. siz bir döngü çalıştırdığınızda o döngü ilk önce o döngüde kullanılacak nesnenin iter metodunu çağırıyor,
# iter metodu bize bize bir iterator dönürüyor ve (for, while) hangi döngüyse bir hata gelene kadar sürekli next metodunu çağırıyor, oradan bir
# hata geldiğini hatayı yakalıyor ve döngüyü sonlandırıyor.

# bir döngü nasıl çalışıyor? yukarıda anlattıklarımı gelin manuel olarak yapmaya çalışalım.
sayilar = [1,2,3]
i_sayilar = iter(sayilar)
while True:
    try:
        sayi = next(i_sayilar)
        print(sayi)
    except StopIteration:
        break                   # 1
                                # 2
                                # 3
# İşte bir döngüde arka planda olan şey aşağı yukarı bundan ibaret. ilk önce bunu oluştur. sonrasında sürekli "next" de, hata aldığın zaman da döngüden çık
# tekrar ediyorum, bir döngü önce iteri çağırıyor, oradan bir iterator alıyor, hata gelene kadar da iterator'un next metodunu çağırıyor. Sayılar
# bittiğinde next metodu "stop iteration" hatası veriyor, dolayısı ile döngümüz de bu hatayı yakalayıp döngüyü sonlandırıyor.

# şimdi bir class oluşturalım, oradan oluşturduğumuz clasın iteratorunu oluşturalım
class New_Range:
    def __init__(self,start,end):
        self.yazilacak = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.yazilacak >= self.end:
            raise StopIteration
        deger = self.yazilacak
        self.yazilacak += 1
        return deger

sayilar = New_Range(10,20)
for i in sayilar:
    print(i)                # 1
                            # 2
                            # 3
# bu şekilde kendi yazdığımız bir clası da döngüler ile kullanabiliriz.
# ne öğrendik?
# iterator, iterable,iteration nedir?
# bir nesnenin iterable olması için içinde iter metodunun bulunması gerekdiğini öğrendik
# iter metodunun bize bir iterator döndürdüğünü öğrendik
# bir nesnenin iterator olabilmesi için next metoduna sahip olması gerektiğini öğrendik
# kendimiz bir class yazdık ve onun içinde bir iter metodu ve bir next metodu tanımladık ve bu sayede itatorun nasıl işlediğini biliyoruz.
# tüm elemanları geziyor ve hangi elemanda kaldığını da aklında tutuyor.
