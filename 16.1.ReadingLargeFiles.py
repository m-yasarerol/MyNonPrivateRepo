# kullanışlı bir kod parçası, çok büyük dosyaları hafızamızı yememesi için parça parça okumak isteyebiliriz. Aşağıdaki kod parçası,
# deneme.txt belgesinin içerisinden 10 adet içerik okuyor, sonrasında bunu tekrar ediyor. dolayısıyla belgenin içerisinin ne kadar ağır olduğunun bir önemi yok.
# verimli bir kullanım
# çünkü bu belge yüksek hacimli bir belge olsaydı ve tek seferde yazdırmaya çalışsaydık cihazımız hafıza problemleri ile karşılaşırdı.
with open("deneme.txt") as f:
    okunacak_miktar = 10
    icerik = f.read(okunacak_miktar)     
    while len(icerik) > 0:              # okunacak bir harf kalana kadar devam eder
        print(icerik, end= "")
        icerik = f.read(okunacak_miktar)
