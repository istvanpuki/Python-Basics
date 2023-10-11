import random

anni_gyozott = 0
panni_gyozott= 0
dobasok_osszege= 0
nyert = ""

#1. feladat

N = int(input("Hány alkalommal legyen feldobás? "))

#2. fealdat

for i in range (N):
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)
    kocka3 = random.randint(1,6)
    dobasok_osszege = kocka1 + kocka2 + kocka3
    
    #3. feladat
    if dobasok_osszege < 10:
        nyert = "Anni"
        anni_gyozott = anni_gyozott + 1
    else:
        nyert= "Panni"
        panni_gyozott= panni_gyozott +1

    print(f"Dobás: {kocka1} + {kocka2} + {kocka3} = {dobasok_osszege} Nyert: {nyert}")

#4. feladat

print(f"A játék során {anni_gyozott} alkalommal Anni, {panni_gyozott} alkalommal Panni nyert")


