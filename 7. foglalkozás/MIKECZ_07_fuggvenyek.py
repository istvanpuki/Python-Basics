#Függvények

def összead_függvény(a,b):
   return a + b

# Mi történik?
#osszead_függvény(2,5)

#És így?
#print( összead_függvény(2,5) )

print( összead_függvény(2,5) )

#Ahhoz, hogy lássuk Pythonban azt az értéket, amit a függvény visszaad, ahhoz a print utasítást szükséges használnunk.
#Legelegánsabb megoldás, hogy ha deklárunk egy új változót, amibe meghívjuk a függvényt és aztán a változót írjuk ki egyszerűen

result = összead_függvény(5,3)
print(result)

def sum():
    numA=int(input("Give the first number: "))
    numB =int(input("Give the second number: "))
    result= numA + numB
    return(f"The correct result is: {result}")

correct_result = sum()
print(correct_result)

#Globális és lokális változók közötti különbség