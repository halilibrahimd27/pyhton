print("""
************************
KULLANICI GİRİŞ PROGRAMI
************************
""")

sys_kulanci_adi = "ibo"

sys_parola = "27467344"

giris_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    parola = input("Parolanızı giriniz:")

    if(kullanici_adi !=sys_kulanci_adi and parola == sys_parola):
        print("Kullanıcı adını hatalı girdiniz.")
        giris_hakki -= 1

    elif(kullanici_adi == sys_kulanci_adi and parola != sys_parola):
        print("Parolayı hatalı girdiniz.")
        giris_hakki -= 1

    elif(kullanici_adi !=sys_kulanci_adi and parola != sys_parola):
        print("Kullanıcı adını ve parolayı hatalı girdiniz.")
        giris_hakki -= 1

    else:
        print("Sisteme başarılı bir şekilde giriş yaptınız.")
        break

    if(giris_hakki == 0):
        print("Daha sonra tekrar deneyiniz...")
        break
