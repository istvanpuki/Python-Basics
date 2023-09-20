import random ## 2. feladathoz importáljuk a Python beépített random package-t
"""
1. feladat
Kérjünk be a billentyűzetről egy egész számot! Ha a szám páros irattassuk ki a dupláját a képernyőre! Ha a szám páratlan akkor
irattassunk ki a képernyőre az adott számtól kettővel kisebb értéket!

2. feladat.
Hozzunk létre egy listát, amit töltsünk fel random egész számokkal 1 és 20 között. A listának 5 eleme legyen!
Irattassuk ki a képernyőre a listából a számokat,
aztán azokat a számokat amik párosak!
"""

print("1. feladat")
userNumber = int(input("A billentyűzetről adj meg egy egész számot! Kattints a konzolon a szöveg mögé! "))
print(userNumber)

if userNumber % 2 == 0:
    print(f"A szám páros és a kétszerese: {userNumber*2}")
else:
    print(f"A szám páratlan és tőle kettővel kisebb: {userNumber-2}")


print("2. feladat")

randomNumbers = []

elementNumber=5

for i in range(elementNumber):
    randomNumbers.append(random.randint(1,20))

print(randomNumbers)

for i in randomNumbers:
    if i % 2 == 0:
        print(i)


