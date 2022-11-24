print("""
************************************
TAM BÖLENLERİNİ BULMA SORGUSUNA HOŞGELDİNİZ.
---------------------------
Programdan çıkmak için '0' a basın.
*************************************
""")


def tambolenleribulma(sayi):

    tam_bolenler = []

    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tam_bolenler.append(i)

    return tam_bolenler

while True:

    sayi = input("Sayi:")

    if(sayi == "0"):
        print("Program sonlandırılıyor...")
        break

    else:
        sayi = int(sayi)
        print("Tam bölenler: ",tambolenleribulma(sayi))
