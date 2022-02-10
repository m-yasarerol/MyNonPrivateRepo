#modüllere ve impor anahtar kelimesini işleyeceğiz.
# modül, çok kullanılan fonksiyonların bir araya getirmesi ile oluşturulmuş pakettir. Siz bu paketi projenize dahil ettikten sonra içerisindeki fonksiyonları kendiniz yazmadan kullanabilirsiniz.
# örneğin birçok sefet faktoriyel fonksiyonun elimizle yazdık.

import math 
sonuc = math.factorial(6)
print(sonuc)
# gördüğün gibi math mdoülünü import ettikten sonra faktoriyel fonksiyonunu yazmama gerek kalmadı.

# Ör: karekok fonksiyonu "sqrt"
sonuc = math.sqrt(65)
print(sonuc)
# yani faktöriyel, karekök, sinüs, kosinus, bunlar çok kullanılan fonk. olduğundan bunları matematik modülü içine  gruplamışlar.

#ör: fabs : mutlak değer fonksiyonu
sonuc = math.fabs(65)
print(sonuc)
# yani modülün bize sağladığı kolaylık budur.

# ancak bazı durumlarda bütün matematik modülünü import etmeyebilirsin. diyelim ki sadece faktoriyel fonksiyonuna ihtiyacimiz var:
from math import factorial
sonuc = factorial()
# bu şekilde tek fonksiyon import edersen doğrudan ismini kullan

# birden fazla fonksiyon import edeceksen:
from math import factorial, sqrt
sonuc = sqrt(5)
print(sonuc)
# bu şekilde birden fazla fonksiyonu ard arda import edebilirsin
# yani from yapısı ile kurduğunuz bir yapı içerden bazı fonksiyonları import etmenize yarar.
# şöyle bir kullanımı da mümkün
from math import *
sonuc = sqrt()
sonuc = fabs()
# yani * import edersen ilk örnekte olduğu gibi "math.sqrt()" şeklinde kullanamazsın ama tüm fonksiyonları yukarıdaki gibi kullanilirsin.

# ben kendi fonkisyonlarımı yazıp bir modül olarak kullanmak istersem. "Matematik modülüm" diye bir dosya oluşturdum. normal bir phyton dosyası. bunun içine 2 adet fonksiyon yazdım. ve onu bu projede kullanacağım.
import benim_matematik_modulum
sonuc = benim_matematik_modulum.cember_cevresi(4)
print(sonuc)

# şöyle de yapabilirdim
from benim_matematik_modulum import cember_cevresi
sonuc = cember_cevresi(4)
print(sonuc)

# diyelim ki modülümün ismi çok uzun, bunları yazmak kalabalığa neden olabilir. böyle bir durumda şunu yapabilirsin.
import benim_matematik_modulum as bmm       #phytona benim matematik modülüm isimli modülü bmm olarak kullanacağım dedim.
sonuc = bmm.cember_cevresi(4)
print(sonuc)

# oluşturduğum modül ve proje aynı klasörde ise birbirini kolayca bulurlar.
# aynı dosyada değiller ise onu gelecek derslerimizde kullanacağız.
# bundan sonraki derslerimizde çok sık kullanacağımız modüllere değineceğiz
# bazılarına değinelim
import os # bu dosya sistemi ile ilgili işler yapabileceğiniz bir modül, yani dosyaları bir yerden bir yere taşımak için kullanabilirsiniz.
import time # saat kaç, bir programın çalışması ne kadar sürdü, ya da program belli bir süre uyku moduna girsin gibi
import datetime # tarih ile ilgili işlemler
# diğer modüller nasıl eklenir?
# bundan sonra phytonda bulunan standart olarak kullanılan önemli modülleri inceleyeğiz.
# sonrasında phytonda standart olarak bulunmayan selenium gibi, pandas gibi değişil modüllere bakacağız. o kısımlar eğlenceli ama karmarşık. buraya kadar işlediğimiz dersleri iyice tekrar yapıp sindirmeniz gerekiyor.
