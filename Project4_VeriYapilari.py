# bu gün mini bir proje yapacağız
# önceki derslerimizde bazı veri yapılarını gördük(listeler , kümeler, stringler, demetler), şimdi bunları listeleyen bir  program hazırlayacağız
# çıktısı başlık- altında metotlar şeklinde olacak. her bir sütunda gerekli olan metotlar sıralanacak
# proje bittikten sonra bir de metin belgesine yazacağız

# ilk olarak listelerin metotlarını almaya çalışalım
list_methods = []
for method in dir(list):                # hatırla, dir, içine mir sınıf yazdığında o sınıfın fonksiyonlarını liste olarak döndürüyordu
    if method.startswith("__"):         # "__" ile başlayan, sık kullanılmayan metotları göz ardı ettim
        continue
    list_methods.append(method)         ##['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# listelerden sonra kümelerin metotlarını alacağım
set_methods = []
for method in dir(set):               
    if method.startswith("__"):        
        continue
    set_methods.append(method)      
# string metotları:
string_methods = []
for method in dir(str):               
    if method.startswith("__"):        
        continue
    string_methods.append(method)  
# tupple(demetler) için:
tupple_methods = []
for method in dir(tuple):               
    if method.startswith("__"):        
        continue
    tupple_methods.append(method)
# Sözlük metotları:
dict_methods = []
for method in dir(dict):               
    if method.startswith("__"):        
        continue
    dict_methods.append(method)    
# her birindeki metotları aldık ve her birisi ayrı ayrı listelerde tutuluyor

basliklar = ["List Methods", "Set Methods", "String Methods", "Tupple Methods", "Dic Methods"]    #başlıkların sırasını karıştırma yoksa metotları birbirinin altına yazar.
classes = [list_methods, set_methods, string_methods, tupple_methods, dict_methods]               # bunların her birisi aslnda birer tane liste
# bütün hepsinde aynı sayıda metot yok, alt alta yazdıracağımız için metot kalmadığı zaman "--" yazsın
max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)
with open("Methods.txt", "w") as f:
    for baslik in basliklar:                #başlıkları yazdırıyorum
        print(baslik,end="")
        print(" " * (30 - len(baslik)),end="")
        f.write(baslik)                     #basliği txt dosyasına yazdırıyorum
        f.write(" " * (30 - len(baslik)))   # yazdığım başlığı 30 karaktere tamamlayana kadar boşluk ekledim
    # bu for döngüsü bittiğinde hangisinde en fazla metot varsa o benim max_len değişkenimin içinde tutulacak
    # hepsi aynı hizada olması adına bir sütun genişliği belirleyelim
    for i in range(max_len):
        print()
        f.write("\n")                       #txt dosyasında satır bittikten sonra entere basar  
        for class_ in classes:
            if i >= len(class_):
                print("-------",end="")
                print(" " * 23,end="")
                f.write("-------")
                f.write(" " * 23)
            else:
                print(class_[i],end="")
                print(" " * (30 - len(class_[i])),end="")
                f.write(class_[i])
                f.write(" " * (30 - len(class_[i])))

#                                                          >> KODUN ÇIKTISI <<

# List Methods                  Set Methods                   String Methods                Tupple Methods                Dic Methods                   
# append                        add                           capitalize                    count                         clear                         
# clear                         clear                         casefold                      index                         copy                          
# copy                          copy                          center                        -------                       fromkeys                      
# count                         difference                    count                         -------                       get                           
# extend                        difference_update             encode                        -------                       items                         
# index                         discard                       endswith                      -------                       keys                          
# insert                        intersection                  expandtabs                    -------                       pop                           
# pop                           intersection_update           find                          -------                       popitem                       
# remove                        isdisjoint                    format                        -------                       setdefault                    
# reverse                       issubset                      format_map                    -------                       update                        
# sort                          issuperset                    index                         -------                       values                        
# -------                       pop                           isalnum                       -------                       -------                       
# -------                       remove                        isalpha                       -------                       -------                       
# -------                       symmetric_difference          isascii                       -------                       -------                       
# -------                       symmetric_difference_update   isdecimal                     -------                       -------                       
# -------                       union                         isdigit                       -------                       -------                       
# -------                       update                        isidentifier                  -------                       -------                       
# -------                       -------                       islower                       -------                       -------                       
# -------                       -------                       isnumeric                     -------                       -------                       
# -------                       -------                       isprintable                   -------                       -------                       
# -------                       -------                       isspace                       -------                       -------                       
# -------                       -------                       istitle                       -------                       -------                       
# -------                       -------                       isupper                       -------                       -------                       
# -------                       -------                       join                          -------                       -------                       
# -------                       -------                       ljust                         -------                       -------                       
# -------                       -------                       lower                         -------                       -------                       
# -------                       -------                       lstrip                        -------                       -------                       
# -------                       -------                       maketrans                     -------                       -------                       
# -------                       -------                       partition                     -------                       -------                       
# -------                       -------                       removeprefix                  -------                       -------                       
# -------                       -------                       removesuffix                  -------                       -------                       
# -------                       -------                       replace                       -------                       -------                       
# -------                       -------                       rfind                         -------                       -------                       
# -------                       -------                       rindex                        -------                       -------                       
# -------                       -------                       rjust                         -------                       -------                       
# -------                       -------                       rpartition                    -------                       -------                       
# -------                       -------                       rsplit                        -------                       -------                       
# -------                       -------                       rstrip                        -------                       -------                       
# -------                       -------                       split                         -------                       -------                       
# -------                       -------                       splitlines                    -------                       -------                       
# -------                       -------                       startswith                    -------                       -------                       
# -------                       -------                       strip                         -------                       -------                       
# -------                       -------                       swapcase                      -------                       -------                       
# -------                       -------                       title                         -------                       -------                       
# -------                       -------                       translate                     -------                       -------                       
# -------                       -------                       upper                         -------                       -------                       
# -------                       -------                       zfill                         -------                       ------- 

# aynı zamanda "methods.txt" isimli bir dosya açıp onun içine yazdırdım.
# ilerki derslerimizde bu kodu daha kısa yoldan yazmayı öğreneceğiz
