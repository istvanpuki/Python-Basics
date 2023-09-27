#Eljarasok

def eljaras():
    print("Ez az első eljárásom.")

def eljaras2(x,y):
    print(x+y)

def eljaras3(keszitette):
    print(f"Az eljárást készítette: {keszitette}")

def eljaras4():
    keszitette =input("Írj ide egy nevet ")
    print(f"Az eljárást készítette: {keszitette}")

def eljaras5():
    osszeg_tag1 =int(input("Adj megy egy számot, amit majd összadok egy másikkal "))
    osszeg_tag2 =int(input("Add meg a második számot "))
    osszeg= osszeg_tag1+osszeg_tag2
    print(f"A pontos összeg: {osszeg}")



eljaras()
eljaras2(5,4)
eljaras3("Nimród")
eljaras4()
eljaras5()

