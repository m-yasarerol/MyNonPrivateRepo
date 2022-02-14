# neden kendilerine ihtiyaç duyuyoruz?
from logging import exception


a = 5
b = 8
c = a / b
print(a)                #5
print(b)                #8
print(c)                #0,62
# sorun yok, peki b' ye sıfır verip çalıştırsaydım?
a = 5
b = 8
c = a / b
print(a)                
print(b)                
print(c)                # Error! : c değişkeni tanımsız oldu. dikkatinizi çekmesi gereken şey şu: biz bu hatayı c de aldık ama bu proint ifadelerinin hiçbirisi çalışmadı, a' yı da b' yi de yazdırmadı
# bunun anlamı şu, siz eğer programın herhangi bir aşamasında bir hata alıyorsanız, programınız çalışmayı durdu demektir. ondan sonraki kodlar herhangi bir şekilde çalışmaz. Eğer siz bir dosya açtıydanız dosya açık kalır veya bir veri tabanına bağlandıysanız veri tabanı bağantısını kesemeyecekseniz veya hiçbirşey olmasa bile programınız çalışmayacak
# dolayısıyla bir bununla baş etmenin yollarını aramaya çalışacağız. yani program bir hata olsa da hemen hata verip kendini sonlandırmasın.
# önce try isminde bir blok oluşturup bu bloğun içine hata üretmesi muhtemel olan kodları yazacağım. ÖR:
try:
    a = 5
    b = 8
    c = a / b
except:
    print("Bir hata oluştu")
print(a,b,c,sep="-")    #5-8-0.625
# herhangi bir hata olmadığı için except bloğunu atlayıp çalışmaya devam etti
# peki şimdi bir hata alacak bir şey yapalım:
try:
    a = 5
    b = 8
    c = a / b
    d = x               # phyton "x"' in ne olduğunu bilmiyor
except:
    print("Bir hata oluştu")
    print("Hatayı düzelten kodlar çalışmalı")
print(a,b,c,sep="-")    # Bir hata olu�tu
                        # 5-8-0.625
# hata oluştuktan sonra programım çalışmaya devam etti. buraada işleyen mantık, bir hata bulunduğunda except blokları içindeki kodlar çalışıyor
# yani mesela siz adamnm adını sordunuz, size adının yerine "23" yazdı, burada kullanıcıya "kullanıcı adınız sayı içermemelidir" şeklinde bir sonuç döndürebilirsiniz.

# hatalar bir şekilde değil de bir sürü şekilde alınabilir. hepsini ayrı ayrı yakalamak istiyorsak:
# yani demek istediğim:
# > mesela 0' a bölme hatası varsa başka bir çözüm üretmemiz gerekiyor
# > kullanıcı isim yerine sayı girdiyse başka bir çözüm üretmemiz gerekiyor
# > bie listenin var olmayan bir elemanına erişmek istiyorsak başka bir çözüm üretmeliyiz
# şimdi bunları ayrı ayrı almaya çalışalım:
# birden fazla çeşitte hata geliyorsa ne yaparım?
try:
    a = 5
    b = 1
    c = a / b
    x = u
    d = x
    isim = "Ali"
    karakter = isim[10]
except ZeroDivisionError:
    print("Payda sıfır olmamalı")
except NameError:
    print("Bu değişken daha önce tanımlanmamış")
except IndexError:
    print("Böyle bir index bulunmuyor")
# except bloklarının hangisi ilk olarak çalıştı ise altındakiler çalışmadı
except Exception:               # genel hata bloğu. belirlediğimin haricindeki hataları kapsar
    print("Bilinmeyen bir hata oluştu")
# dikkat et. genel hata bloğunu en başa koyarsan bir hata olduğunda direkt oraya yakalanır
# o yüzden biz böyle bir şey yapacaksak ilk önce tahmin ettiğimiz except bloklarını yazmalıyız

# else bloğu
try:
    a = 5
    b = 1
    c = a / b
    x = 1
    d = x
    isim = "Ali"
    karakter = isim[2]
except ZeroDivisionError:
    print("Payda sıfır olmamalı")
except NameError:
    print("Bu değişken daha önce tanımlanmamış")
except IndexError:
    print("Böyle bir index bulunmuyor")
except Exception:
    print("Bilinmeyen bir hata oluştu")
else:                               # else bloğu herhangi bir except bloğu çalışmadığında çalışır. yani try bloğunun içinde hrhangi bir hata olmadığında çalışır.
    print("Else bloğu çalışıyor")
    print(c)
    print(karakter)
finally:                            # bir hata olsa da olmasa da çalışır. 
    print("Finally bloğu çalışıyor")
# tekrar edelim:
# eğer try'da bir hata olursa o hataya karşlık olan except bloğu çalışıyor
# eğer herhangi bir hata bulamadıysak en sona yazdığımız genel hata bloğu çalışacak
# eğertry'da herhangi bir hata yoksa else bloğu çalışır
# finalli bloğu ise her türlü çalışır

# bazen raise anahtar kelimesini kullanarak bilinçli olarak da hata üretebilirim
# Ör:
try:
    a = 5
    b = 0
    if b == 0:
        raise ZeroDivisionError # << b benim belirlediğim koşula uygunsa ona göre bir hata fırlatabilirim
    c = a / b
    x = 1
    d = x
    isim = "Ali"
    karakter = isim[2]
except ZeroDivisionError:
    print("Payda sıfır olmamalı")
except NameError:
    print("Bu değişken daha önce tanımlanmamış")
except IndexError:
    print("Böyle bir index bulunmuyor")
except Exception:
    print("Bilinmeyen bir hata oluştu")
else:                              
    print("Else bloğu çalışıyor")
    print(c)
    print(karakter)
finally:                           
    print("Finally bloğu çalışıyor")

# hatalara "as" ile değişken atayarak o hatanın varsayılan mesajın yazdırabilirim
try:
    a = 5
    b = 1
    c = a / b
    x = 1
    d = x
    isim = "Ali"
    karakter = isim[2]
except ZeroDivisionError as e:
    print("Payda sıfır olmamalı")
except NameError as e:
    print(e)                            # name eror'un varsayılan mesajı döner
except IndexError as e:
    print(e)                            # index erorun varsayılan mesajı döner
except Exception as e:
    print(e)                            # ilgili hatanın varsayılan mesajı döner
else:                               
    print("Else bloğu çalışıyor")
    print(c)
    print(karakter)
finally:                            
    print("Finally bloğu çalışıyor")

# try içindeki kodlar hata verme ihtimali olan kodlar olacak, eğer orada hata çıkarsa except bloklarından uygun olanına atlayacak, eğer hata çıkmazsa else bloğuna atlayacak, ve finally bloğu da her ne olursa olsun çalışacak
