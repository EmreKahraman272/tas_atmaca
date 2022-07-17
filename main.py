import math
import random
from yukseklik import yukseklik

puan = 0
deneme = 3
mesafe = 100
a = random.randint(30,170)

while deneme > 0:
    aci = int(input("Açı giriniz:"))
    hiz = int(input("Hız giriniz:"))
    y = yukseklik(aci, hiz, mesafe)
    if (0 <(abs(a-y))<= 10):
        puan = puan + 4
        deneme = deneme - 1
        print("hakkınız:",deneme)
        print("İsabet noktası: ",abs(a - y))
        print("Nişangah yeri: ",a)
        print("Puanınız:",puan)
    elif (10 <(abs(a-y))<= 20):
        puan = puan + 3
        deneme = deneme - 1
        print("hakkınız:", deneme)
        print("İsabet noktası: ", abs(a - y))
        print("Nişangah yeri: ", a)
        print("Puanınız:", puan)
    elif (20 <(abs(a-y))<= 30):
        puan = puan + 2
        deneme = deneme - 1
        print("hakkınız:", deneme)
        print("İsabet noktası: ", abs(a - y))
        print("Nişangah yeri: ", a)
        print("Puanınız:", puan)
    elif (30 <(abs(a-y))):
        puan = puan + 1
        deneme = deneme - 1
        print("hakkınız:", deneme)
        print("İsabet noktası: ", abs(a - y))
        print("Nişangah yeri: ", a)
        print("Puanınız:", puan)