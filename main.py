import math
import random


puan = 0
deneme = 3

while deneme > 0:
    a = random.randint(1, 200)
    b = 120
    if (0 <(abs(a-b))<= 10):
        puan = puan + 4
        deneme = deneme - 1
        print("hakkınız:",deneme)
        print(abs(a - b))
        print(a)
        print("Puanınız:",puan)
    if (10 <(abs(a-b))<= 20):
        puan = puan + 3
        deneme = deneme - 1
        print("hakkınız:", deneme)
        print(abs(a - b))
        print(a)
        print("Puanınız:", puan)
    if (20 <(abs(a-b))<= 30):
        puan = puan + 2
        deneme = deneme - 1
        print("hakkınız:", deneme)
        print(abs(a - b))
        print(a)
        print("Puanınız:", puan)
    if (30 <(abs(a-b))):
        puan = puan + 1
        deneme = deneme - 1
        print("hakkınız:", deneme)
        print(abs(a-b))
        print(a)
        print("Puanınız:", puan)