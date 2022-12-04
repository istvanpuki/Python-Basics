# Python List (Mi az a python lista? Más programozási nyelvekben tömbnek hívják a listákat)

# Akik emlékeznek arra, hogy a változókat a dobozos példával szemléltettük, azok maradhatnak ezen a logikai útvonalon.

# A tömböt (pythonban lista) elképzelhetjük egy olyan változónak, ami képes egymás mellett eltárolni sok-sok értéket.

# Egy dobozban több érték is lehet. De a dobozban kisebb karton válaszfalak elválasztják egymástól a változókat.

# A San Francisco-ból jöttem Youtube csatonája egy kiváló videóval szemlélteti ezt, nézd meg, ha érdekel!

# A következő példákban márkaneveket fogunk felsorolni egy listában.

# A listákat kapcsos zárójellel hozzuk létre. Így hozunk létre egy üres listát

brands = [] # Üres lista

# A Pyton listák különlegessége, hogy többféle típusú értéket tárolhat. Például lehetnek benne stringek és integer típusú változók is.
# Más programozási nyelvekben is előfordul ez, de pl. javaban, c#-ban nem csinálhatsz ilyet.

# Az append() metódus segítségével fűzünk elemeket a listába. Az append() mindig a lista végéhez ad hozzá egy elemet az alábbi példában.

brands.append("Acer")
brands.append("Intel")
brands.append("Asus")
brands.append("AMD")
brands.append("HP")

print(brands)

# Szemléltessük, hogy többféle típusú változó is lehet egy tömbben. Ha nem muszáj, akkor ezt a megoldást kerüljük a jövőben.
# Clean Code elv miatt

brands.append(1)
brands.append(2)
brands.append(3)

print(brands)

brands.remove(3)
print(brands)

# brands.clear()  - ez kitörölne minden elemet a listából

# Listák indexelése

# A programozásban a lista első elemére általában a 0. elemként tudunk hivatkozni.

# Egész egyszerűen a lista elemeinek sorszámozását nem 1-től, hanem 0-tól kezdik. Ez az elején összezavarhat, de majd megszokjátok! :)

# Beszúrás a tömbbe (listába)
brands.insert(5, "Coca-Cola")  #A szám az jelenti, hogy hanyadik elem legyen a listába a Coca-col. 0-tól indul a számozás
# Ha én azt akarom, hogy a 6. elem legyen a képernyőn, akkor az a listában az 5. elem lesz. Mert az Acer a 0. elem
print(brands)

brands.reverse()  #lista megfordítása
print(brands)


numbers = [15, 8, 78, 23, 1, 65, 184]
print(numbers)
numbers.sort()  #növekvő sorrendben
print(numbers)
numbers.reverse() #csökkenő
print(numbers)
#sort csak akkor használható ha csak számokból vagy betűkből áll

firstNames = ["Xéna", "Bözsi", "Vica", "Enikő", "Ildi"]
firstNames.sort()
print(firstNames)
print(len(firstNames)) #lista hosszúságát írta ki, hogy hány elem van benne. a length szóra utal