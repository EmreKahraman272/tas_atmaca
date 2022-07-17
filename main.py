import math
import random
from yukseklik import yukseklik

puan = 0
deneme = 3
mesafe = 100
a = random.randint(30,170)

while deneme > 0:
    print("Nişangah yeri: ", a)
    aci = int(input("Açı giriniz:"))
    hiz = int(input("Hız giriniz:"))
    y = yukseklik(aci, hiz, mesafe)
    if (0 <(abs(a-y))<= 10):
        puan = puan + 4
        deneme = deneme - 1
        print("Kalan atış hakkınız:",deneme)
        print("Nişangah merkezine olan uzaklığınız: ",abs(a - y))
        print("Puanınız:",puan)
    elif (10 <(abs(a-y))<= 20):
        puan = puan + 3
        deneme = deneme - 1
        print("Kalan atış hakkınız:", deneme)
        print("Nişangah merkezine olan uzaklığınız: ", abs(a - y))
        print("Puanınız:", puan)
    elif (20 <(abs(a-y))<= 30):
        puan = puan + 2
        deneme = deneme - 1
        print("Kalan atış hakkınız:", deneme)
        print("Nişangah merkezine olan uzaklığınız: ", abs(a - y))
        print("Puanınız:", puan)
    else:
        puan = puan + 1
        deneme = deneme - 1
        print("Kalan atış hakkınız:", deneme)
        print("Nişangah merkezine olan uzaklığınız: ", abs(a - y))
        print("Puanınız:", puan)