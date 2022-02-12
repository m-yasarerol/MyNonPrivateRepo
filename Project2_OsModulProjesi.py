# BU DERSİ ANLAMADIM
#  proje, içinde karşılık belgeler bulunduran bir klasörü içindeki belgelerin uzantısına göre snıflandıran bir yazılımdır. 
import os
#projeyi bir düzenle fonkisyonunun içine yazacağım, böylece gerektiğinde başka yerde import edip kullanabileceğim

def düzenle():
    klasor = input("Düzenlenecek klasör: ")
    dosyalar = []                                           #dosyalar depolanacak
    uzantılar = []                                          #uzantılar dapolanacak
    def list_dir():                                         # listdir yerine bunu kullandım yeni bir fonk. oluşturdum çünkü ben bu klasörün içindeki dosyaları sınıflandırmak istiyorum. yani bunun içinde eğer var olan klasörler varsa onlara herhangi bir şey yapmak istemiyorum. bu yeni oluşturduğum fonkisyon eğer bir klasörle karşılaşırsa onu es geçecek, dosyalar listesine eklemeyecek
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)):   # dosyamız bir klasör mü?
                continue
            if dosya.startswith:("."):                      #dosyamız bir gizli dosya mı?
                continue
            else:                                           #ikisi de değilse dosyamızı dosyalar klasörüne ekle
                dosyalar.append(dosya)         
    list_dir()
    # uzantıları alma
    # şimdiki yapacağım işlem bu klasörde bulunan dosyaların uzantılarını almak
    for dosya in dosyalar:
        uzanti = dosya.split(".") [-1]
        if uzanti in uzantilar:                             #uzantı daha önce eklendi mi?
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantılar:                            #klasörler oluşturuluyor
        if os.path.isdir(os.path.join(klasor,uzanti)):  # bu true dönerse zaten öyle bir klasör var demektir
            continue
        else:
            os.mkdir(os.path.join(kalsor,uzanti))
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor,dosya), os.path.join(klasor,uzanti,dosya))
if __name__ ==" __main__ ":
    duzenle()
