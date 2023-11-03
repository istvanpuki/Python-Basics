itemsWeights = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
sumWeights = 0

for item in itemsWeights:
    sumWeights = sumWeights + item

print(f"2. feladat \nA tárgyak tömegének összege: {sumWeights} kg\n ")

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
print("A dobozok tartalmának tömege (kg): ", *boxes) 
print(f"A szükséges dobozok száma: {len(boxes)}")
  
