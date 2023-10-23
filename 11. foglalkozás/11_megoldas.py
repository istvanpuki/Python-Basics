# 11-es feladat
"""
Írj egy programot, ami a billentyűzetről bekér egy számot. Ez a szám a dolgozatod eredménye százalékban kifejezve. A programnak
meg kell adnia, hogy hanyas érdemjegyet szereztél az alábbiak szerint:

A dolgozatok szöveges értékelése: 
0 % ... 30 % - nem felelt meg
30 % ... 75 % - megfelelt
75 % ... 100 % - jól megfelelt

Ezt a szöveget kell látnod a konzolon, miután elindítod a programot:

Add meg az elért egész pontszámodat, ami 0 és 100 között lehet:

"""

def pontszamitas(pontszam):
    pontszam = int(pontszam)

    if pontszam > 0 and pontszam <= 30:
        print()
        print(f"Elért pont százalékban {pontszam}%. - Nem felelt meg.")
    elif pontszam > 30 and pontszam <= 75:
        print()
        print(f"Elért pontszám százalékban {pontszam}% - Megfelelt. ")
    elif pontszam > 75:
        print()
        print(f"Elért pontszám százalékban {pontszam}% - Jól megfelelt.")

pontszamitas(input("Add meg az elért egész pontszámodat, ami 0 és 100 között lehet: "))