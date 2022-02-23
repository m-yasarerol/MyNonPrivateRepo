# Bu proje, bilgilerinizi girdiğinizde sizin için vücut kitle endexini hesaplayan bir uygulamadır. Herhangi bir yerden yardım almadan ben yaptım.
def index_(x,y):
    return x / (y * y)
isim = input("Merhaba! ben tele diyetisyen, isminiz nedir? : ")
boy = int(input(f"Hoşgeldin {isim}, boyunuz (cm):"))
kg = int(input("Kilonuz (kg): "))
boy_m = boy / 100                             #"cm" cinsinden girilen boy bilgisini "metre" cinsine dönüştürdüm.
hesaplanan_index = index_(kg,boy_m)           # kullanıcıdan aldığım bilgileri fonksiyona gönderdim.
hesaplanan_index = round(hesaplanan_index,1)  # hesaplanan index için virgülden sonra 1 basamak aldım.
if hesaplanan_index > 0 and hesaplanan_index <= 18.4:
    print(f"{isim}, boy kilo endeksini {hesaplanan_index} olarak hesapladım.İdeal kilonun altnda kalmışsın , tek ihtiyacın biraz motivasyon biraz da dengeli beslenmek.")
elif hesaplanan_index >= 18.5 and hesaplanan_index <= 24.9:
    print(f"{isim}, boy kilo endeksini {hesaplanan_index} olarak hesapladım. Kilon ideal. Şimdi sana bunu korumak düşüyor. Harikasın!")
elif hesaplanan_index >= 25 and hesaplanan_index <= 29.9:
    print(f"{isim}, boy kilo endeksini {hesaplanan_index} olarak hesapladım. İdeal kilonun üzerindesin. Ama hedefe yakınsın! önünde kısa bir yol var, anahtar kelimeler dengeli beslenme ve spor :)")
elif hesaplanan_index >=30 and hesaplanan_index <= 34.9:
    print(f"{isim}, boy kilo endeksini {hesaplanan_index} olarak hesapladım. İdeal kilonun çok üzerindesin. Uzman bir sağlık kuruluşuna gitmeni tavsiye ediyorum.")
else:
    print(f"{isim}, boy kilo endeksini {hesaplanan_index} olarak hesapladım. İdeal kilonun çok üzerindesin. Uzman bir hekim desteğine başvurmalısın.")
