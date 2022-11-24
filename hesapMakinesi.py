print("""
*************************
HESAP MAKİNESİ UYGULAMASI
-------------------------
İŞLEMLER:

1. TOPLAMA
2. ÇIKARMA
3. ÇARPMA
4. BÖLME
5. KAREKÖK ALMA
6. YÜZDE ALMA
7. MOD ALMA
8. FAKTÖRİYEL ALMA
9. ÜS ALMA
-------------------------
Pogramdan çıkmak için "0" a basın.
*************************""")

while True:

    islem = input("Yapmak istediğiniz işlemi seçiniz:")

    if(islem == "0"):
        print("Program kapatılıyor...")
        break

    elif(islem == "1"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        toplam = sayi1 + sayi2
        print("Sayıların toplamı: {}".format(toplam))

    elif(islem == "2"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        cikarma = sayi1 - sayi2
        print("Sayıların çıkarımı: {}".format(cikarma))

    elif(islem == "3"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        carpma = sayi1 * sayi2
        print("Sayıların çarpımı: {}".format(carpma))

    elif(islem == "4"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        bolme = sayi1 / sayi2
        print("Sayıların bölümü: {}".format(bolme))

    elif(islem == "5"):
        sayi1 = int(input("Sayı:"))
        karekok = sayi1 ** 0.5
        print("Sayının karekökü: {}".format(karekok))

    elif(islem == "6"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        yuzde = (sayi2 *100) /sayi1
        print("Sayıların yüzdesi: {}".format(yuzde))

    elif(islem == "7"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        mod = sayi1 % sayi2
        print("Sayıların modu: {}".format(mod))

    elif(islem == "8"):
        faktoriyel = 1
        x = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz:"))

        for i in range(1, x + 1):
            faktoriyel = faktoriyel * i
        print(faktoriyel)

    elif(islem == "9"):
        sayi1 = int(input("Sayı:"))
        sayi2 = int(input("Sayı:"))
        us = sayi1 ** sayi2
        print("Sayıların üssü: {}".format(us))

    else:
        print("Hatalı tuşlama yaptınız...")
