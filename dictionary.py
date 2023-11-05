dictionary = {
    "bilgisayar": "Elektronik bir cihaz",
    "kütüphane": "Kitapların saklandığı yer",
    "kahve": "Sıcak içecek",
    "yürüyüş": "Yavaş ve düzenli adımlarla yürümek",
    "güneş": "Gündüz gökyüzünde görülen parlak yıldız"
}

while True:

    girilenKelime = input("Bir kelime giriniz ")

    if girilenKelime in dictionary:
        print(girilenKelime.upper() + " : " + dictionary[girilenKelime])
    else:
        print(girilenKelime + " : sözlükte bulunamadı")    
        cevap = input("bu kelimeyi eklemek ister misiniz? evet/hayır : ")
        if cevap == "evet":
            eklenen = input(girilenKelime + "'nın tanımını giriniz : ")
            dictionary[girilenKelime] = eklenen 
            print(girilenKelime + ":" + eklenen)
            print("listeye eklendi")

            # gnclSozluk = input("sozlugun guncel halini gormek ister misiniz ? evet/hayır : ")
            # if gnclSozluk == "evet":
            #     for anahtar in sorted(dictionary):
            #      print(anahtar + " : " + dictionary[anahtar])
                
            for anahtar in sorted(dictionary):
                print(anahtar + " : " + dictionary[anahtar])
                
        else:
            break            
            
            
             
              


