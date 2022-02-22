# bir önceki derste öğrendiğimiz bilgileri uygulamaya geçeceğiz. kendimiz bir class oluşturup bu clas'ı for döngusu yardımıyla kullanılabilir bir hale getircez
# yani kendi iteratorumuzu yazacağız.

cumle = "Merhaba benim adım Yaşar"
for i in cumle:
    print(i)        # harf harf yazdırdı. ama ben kelime kelime yazmasını istiyorum. dolayısıyla bunu yapmak için benim kendi iteratorumu oluşturmam gerekiyor.
# yani bir class oluşturacağız. o clasın nesnelerini for döngüsü ile yazdırdığımızda ekrana harf harf değil de kelime kelime yazdıracak

class Cumle:        # önce kendi clasımı oluşturmalıyım
    def __init__(self,cumle):
        self.cumle = cumle          # bu clasın nesnesi cümle isminde bir string ifadeye sahip
        self.index = 0
        self.kelimeler = self.cumle.split(" ")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.kelimeler):
            raise StopIteration
        dondurulecek = self.index 
        self.index += 1             ## yazdırılacak olan indexi belirle, sonra indexi bir arttır. sonra ESKİSİNİ YAZDIR. BU SAYDEDE NEXT METODU BİR DAHA ÇAĞRILDIĞINDA BİR SONRAKİ KELİMEYİ YAZDIRMIŞ OLUYORUM.
        return self.kelimeler[dondurulecek]

yenicumle = Cumle("Merhaba, hepiniz hoş geldiniz.")
for kelime in yenicumle:
    print(kelime)   # Merhaba,
                    # hepiniz
                    # ho�
                    # geldiniz.
# bu şekilde gördük ki, biz kendi oluşturduğumuz bir clası da for döngüsü ile kullanılabilir bir hale getiriyoruz. bunun için yapmamız gereken şey
# bu nesnenin for döngüsü ile kullanılabilmesini sağlayan iter metodunu tanımlamak, bu iter metodu bize bir iterator döndürüyordu.kendisi bir iterator olacaksa next metoduna sahip olması gerekiyordu
# onu da tanımladık, eğer yazdırılacak elemanlar bitti ise stop iteration hatasını göndererek döngünün sonlanmasını sağlıyoruz.
