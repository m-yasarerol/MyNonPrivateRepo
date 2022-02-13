#  Bu proje çok önemli çünkü bu güne kadar öğrendiğimiz her şeyi kullanıcaz
#  bu proje için gereklilikler
# >dosyaları okuma/yazma
# >listeler
# >stringler
# >döngüler
# PROJE TANITIMI:örenci isim, bölüm bilgisi ve not bilgisi var. programımız çalıştığında kalanlar ve geçenler için ayrı dosya oluşturup öğrencileri puanlarına göre dosyalara yerleştirip, geçti-kaldı yazacak
# geçip kaldığına nasıl karar verecek? 
#  1. vize %30,
#  2.vize %30,
#  final %40 etkili olacak şekilde:
# ek olarak finalden de en az 70 puan alması gerekmektedir.
# yapacağımız şey listeyi okuyacağız, isim soy isim / bölüm / notlar kısmını ayıracağız
# problem: isim ve bölüm bilgileri bazen 1, bazen 2 kelimeden oluşuyor
with open("ornek_metin.txt") as f:
    with open("gecenler.txt", "w") as g:
        with open("kalanlar.txt", "w") as k:
            icerik = f.readlines()
            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n", "")         #replace bazı karakter gruplarını başka bir karakterle değiştirmei sağlar
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0 
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]         # ad ve soyadlar - ile bölündüğü için -'yi split ettim. soyad son eleman olduğundan index numarasına -1 ile ulaştım
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                birinci_vize = int(notlar[0])           #string veriyi integere çevirdim çünkü matematiksel işlemler yapcam
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                ortalama = birinci_vize * 0.3 + ikinci_vize * 0.3 + final * 0.4
                bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[len(bosluk_indexleri) - 1]]  #bölüm, ilk boşluk ile son boşluğun arasını ifade eder.
                if ortalama >= 70 and final >= 70:
                    g.write(ad)
                    g.write(" " * (25 - len(ad)))
                    g.write(soyad)
                    g.write(" " * (25 - len(soyad)))
                    g.write(bolum)
                    g.write(" " * (25 - len(bolum)))
                    g.write(str(round(ortalama,1)))
                    g.write(" " * 21)
                    g.write("Geçti")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (25 - len(ad)))
                    k.write(soyad)
                    k.write(" " * (25 - len(soyad)))
                    k.write(bolum)
                    k.write(" " * (25 - len(bolum)))
                    k.write(str(round(ortalama,1)))
                    k.write(" " * 21)
                    k.write("kaldı")
                    k.write("\n")
