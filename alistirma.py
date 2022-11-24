#********anlıkTarihveSaat*********

import datetime

e = datetime.datetime.now()

print ("Güncel tarih ve saat = %s" %e)
print ("Bugünün tarihi:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("Saat: = %s:%s:%s" % (e.hour, e.minute, e.second))


#*********mukemmelsayı***********

sayi = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayi):
    if (sayi % i == 0):
        toplam += i
    i += 1

if (toplam == sayi):
    print(sayi,"mükemmel bir sayıdır.")
else:
    print(sayi,"mükemmel bir sayı değildir.")
    
    
#********armstrongsayı********
sayi = input("Sayı:")
basamak_sayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

gecici_sayi = sayi

while (gecici_sayi > 0):
    basamak = gecici_sayi % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayi //= 10

if (toplam == sayi):
    print(sayi, "bir armstrong sayısıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")

