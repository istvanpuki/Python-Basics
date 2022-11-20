#Változók használata a gyakorlatban, Tipusok
#Number, String, Boolean, (Gyakran használt típusok)

#Mi a változó? https://www.youtube.com/watch?v=VRt0hViU5kY&t=172s
# Ez egy fantasztikus videó. A változóról nyugodtan eszedbe juthat egy doboz. A Python egy dinamikusan típusos nyelv, ezért kezdetben
# könnyű dolgunk van a változók létrehozásukkal, kezelésükkel.

#Változónak mindig van
#Neve
#Értéke
#Típusa

#Érdemes értéket adnunk a változóknak létrehozásukkor
#Ha ezt nem tesszük meg, akkor értéke undefined lesz. (Még nem nyitottuk ki a dobozt)
#Ha már kinyitottuk és a dobozt üresen hagyjuk, akkor lesz null értéke.
#A null nem egyenlő a 0 értékkel

#Number típus
szam_a = 10 #number int
szam_b = 8.24 #number float
szam_c = 32.3e19 #number tudomanyos
szam_d = .825j #number komplex

favourite_number = 99 # Ez Javaban úgy nézne ki, hogy    int favourite_number = 99;
# Láthatod, hogy Pythonban nem kell megadni a változó típusát, mert arra az interpreter magától következtet az értékből.
# Ennek komolyabb projektek esetén lehet hátránya, hogy bizonyos műveletek esetén nem megfelelő típushasználat miatt nem várt eredményt kapunk.

print(szam_a)
print(type(szam_a))
print(type(szam_b))

#String típus (karaktersorozat)
nev = "Roland" #string
auto = "Seat" #string
mondat = "néha elmegy futni." #string

print(nev)
print(mondat)
print(nev+" "+mondat)

#Boolean (igaz vagy hamis)
igaz = True
hamis = False
print(type(igaz))

age = 5
print(f"John is {age} years old")
# Ezzel a módszerrel átláthatóbb a változók kiiratása egy sztringen belül.

# A programozás világában a változóknak angol neveket szoktunk adni. Figyeljünk arra, hogy a változó neve utaljon a tartalomra.
# A kezdetekben még magyar neveket fogunk adni a változóknak, hogy könnyebb legyen értelmezni a feladatokat.
# Oldjuk meg a következő feladatokat a gyakorlatban.
# https://www.w3schools.com/python/exercise.asp?filename=exercise_comments1 A kommentekről 2 rövid feladat.
# https://www.w3schools.com/python/exercise.asp?filename=exercise_variables1 Változók használata

# Mi fog történni a következő példákban? Vizsgáljuk meg!

x = 5
y = "John"
z = "3"
w = 2

"""
print(x+w)
print(x+y)
print(x+z)
print(x+y+z+w)
"""
# A print(x+z) művelet esetén kiszűrhető valahogy a hiba? Egy kulcsszót adok segítségként. Típuskényszerítés. Várom a megoldásokat! :)
# Kezdj el keresni a Google felületén! Magyarul is találsz hasznos anyagokat, de próbálj meg angolul keresni.
# A kényszerítés helyett az átalákulás lehet a kulcsszó angolul.

# Következő órán megismerkedünk a Listákkal (List) és a Tuple adatszerkezettel.