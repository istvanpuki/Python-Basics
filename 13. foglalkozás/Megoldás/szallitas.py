#1. feladat Eltároljuk a 15 számot egy megfelelő adatszerkezetben.
itemsWeights = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
#print (itemsWeights)

#2. feladat
sumWeights = 0

for item in itemsWeights:
    #print(item)
    sumWeights = sumWeights + item

print(f"2. feladat \nA tárgyak tömegének összege: {sumWeights} kg\n ")

#3. feladat
boxes = []
count = 0

for item in itemsWeights:
    if count + item < 21:
        count = count + item
    else:
        boxes.append(count)
        count = 0
        count = count + item

boxes.append(count)

print("3. feladat")
print("A dobozok tartalmának tömege (kg): ", *boxes) #Csillag operátor használata a kiíratás miatt
print(f"A szükséges dobozok száma: {len(boxes)}")
  
