# dosyaları tarihlere göre sınıflandırmak
# eski projeden yararlanacağız çünkü bazı kısımlar ortak olacak
import os
from datetime import datetime
def düzenle():
    klasor = input("Düzenlenecek klasör: ")
    dosyalar = []                                           #dosyalar depolanacak
    tarihler = []                                           #tarihler dapolanacak
    def list_dir():                                         # listdir yerine bunu kullandım yeni bir fonk. oluşturdum çünkü ben bu klasörün içindeki dosyaları sınıflandırmak istiyorum. yani bunun içinde eğer var olan klasörler varsa onlara herhangi bir şey yapmak istemiyorum. bu yeni oluşturduğum fonkisyon eğer bir klasörle karşılaşırsa onu es geçecek, dosyalar listesine eklemeyecek
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)):   # dosyamız bir klasör mü?
                continue
            if dosya.startswith("."):
                continue
            else:                                           #ikisi de değilse dosyamızı dosyalar klasörüne ekle
                dosyalar.append(dosya)         
    list_dir()
    # tarihleri alma: os.stat ile alıyordum
    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor,dosya)) #bana bir tarih damgası döndürecek, okunabilir değil
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")     # saniyeler farklı old . için her dosya için ayrı klasor açıcak, ben bunu istemiyorum. aynı gün açılan dosyaları aynı klasöre alsın. bunun için strf time ' i kullandım
        if tarih in tarihler:                               # eğer bu tarih zaten eklendiyse..
            continue                                        # herhangi bir şey yapma
        else:                                               # daha önce eklenmediyse tarihler listesine ekle
            tarihler.append(tarihler)
    for tarih in tarihler:                            #klasörler oluşturuluyor
        if os.path.isdir(os.path.join(klasor,tarih)):  # bu true dönerse zaten öyle bir klasör var demektir
            continue
        else:
            os.mkdir(os.path.join(kalsor,tarih))
    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor,dosya)).st_birthtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")     
        os.rename(os.path.join(klasor,dosya), os.path.join(klasor,tarih,dosya))
if __name__ ==" __main__ ":
    duzenle()

# strf time ile okunabilir hale getirdim.
