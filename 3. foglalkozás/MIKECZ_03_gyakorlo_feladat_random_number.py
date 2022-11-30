import random

"""
a = random.random()
a = random.randint(1,5)
print(a)
"""

number_a = random.randint(1,5)
number_b = random.randint(1,5)

# print(number_a, number_b)

if (number_a == number_b):
    print(f"A két szám egyenlő mert A értéke {number_a} és B értéke {number_b}") 
else:
    print(f"A két szám nem egyenlő mert A értéke {number_a} és B értéke {number_b}")


"""
Feladat: Hozz létre két változót, amiknek értékei egész számok legyenek 1 és 5 között, de ezek
az értékek véletlenszerűen generálódjanak minden egyes programfutattással.
Vizsgáljuk meg, hogy a 2 változó értéke mikor egyenlő. Írjuk ki a képernyőre az értékeket
egy kisérőszöveggel, hogy egyenlőek az értékek vagy nem.
"""