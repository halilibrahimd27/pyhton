print("""
************************************
ATM MAKİNESİNE HOŞGELDİNİZ.
---------------------------
İşlemler:
1. Bakiye Sorgulama
2. Para Yatırma 
3. Para Çekme
4. Nakit Avans

Programdan çıkmak için '0' a basın.
*************************************
""")

bakiye = 1000
nakit_avans_limiti = 750

while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz:")

    if(islem == "0"):
        print("Yine bekleriz.")
        break

    elif(islem == "1"):
        print("İşleminiz gerçekleştiriliyor...\nİşlem başarıyla tamamlandı.\nGüncel bakiyeniz: {}".format(bakiye))

    elif(islem == "2"):
        a = int(input("Yatırmak istediğiniz tutarı giriniz:"))
        yeni_bakiye = a + bakiye
        print("İşleminiz gerçekleştiriliyor...\nİşlem başarıyla tamamlandı.\nYeni bakiyeniz: {}".format(yeni_bakiye))

    elif(islem == "3"):
        a = int(input("Çekmek istediğiniz tutarı giriniz:"))
        yeni_bakiye = bakiye - a

        if(bakiye - a < 0):
            print("Yetersiz bakiye.")
        else:
            print("İşleminiz gerçekleştiriliyor...\nİşlem başarıyla tamamlandı.\nYeni bakiyeniz: {}".format(yeni_bakiye))

    elif (islem == "4"):
        b = int(input("Çekmek istediğiniz nakit avans tutarını giriniz:"))
        nakit_avans_limiti -= b

        if (nakit_avans_limiti - b < 0):
            print("Yetersiz bakiye.")
        else:
            print("İşleminiz gerçekleştiriliyor...\nİşlem başarıyla tamamlandı.\nKalan nakit avans bakiyeniz: {}".format(nakit_avans_limiti))

    else:
        print("Geçersiz işlem...")
