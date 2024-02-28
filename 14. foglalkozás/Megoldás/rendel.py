# 1. Exercise
orders = []
order = {}

with open('rendel.txt', 'r', encoding='utf-8') as file:
    for row in file:
        dataRow = row.strip().split()

        order = {
            'orderDay': int( dataRow[0] ),
            'orderCity': dataRow[1],
            'orderPiece': int( dataRow[2])
        }
        
        orders.append(order)
#print(orders)

# 2. Exercise
print(f"2. feladat: \nA rendelések száma: { (len (orders) ) }")

# 3. Exercise
def ordersNumber(orderNumber):
    sum = 0
    for order in orders:
        if orderNumber == order['orderDay']:
            #print(order['orderDay'])
            sum = sum + 1
    return sum

ordersnumber = ordersNumber(int( input("Kérem adjon meg egy napot: ") ) ) 
print(f"A rendelések száma az adott napon: {ordersnumber} ")

# 4. Exercise
orderDays = set() # Set is useful to us, because this method doesn't let the items to repeat themselves. 4example: Day1 only add once.
missingDays = 0
def noCommercialCity():   
    for order in orders:
        if order['orderCity'] == 'NR':
            orderDays.add(order['orderDay'])

        missingDays = 30 - len(orderDays)
    
    if missingDays == 0:
        return "Minden nap volt rendelés a reklámban nem érintett városból"
    else:
        return missingDays

print("4. feladat:") 
nocommercialcity = noCommercialCity()
print(f"{nocommercialcity} nap nem volt a reklámban nem érintett városból rendelés")

#5. Exercise nincs kész
def maxPiece():
    biggestPiece = 0
    orderDay = {}
    for order in orders:
        if order['orderPiece'] > biggestPiece:
            biggestPiece = order['orderPiece']
            orderDay = order
    return f"A legnagyobb darabszám: {biggestPiece}, a rendelés napja: {orderDay['orderDay']} "

print("5. feladat: ")
maxpiece = maxPiece()
print(f"{maxpiece}")

# Exercise 6. 

def osszes(cityName, day):
    counter = 0
    for order in orders:
        if order['orderCity'] == cityName and order['orderDay'] == day:
           counter += order['orderPiece']
    return counter

osszes = osszes( str( input("OrderCity: ") ), int( input("OrderDay: ") ) )
print(osszes)

# Exercise 7.

def exerciseSeven():
    counterPL = 0
    counterNR = 0
    counterTV = 0
    PL = "PL"
    NR = "NR"
    TV= "TV"

    for order in orders:
        if order['orderCity'] == PL and order['orderDay'] == 21:
           counterPL += order['orderPiece']
        if order['orderCity'] == NR and order['orderDay'] == 21:
           counterNR += order['orderPiece']
        if order['orderCity'] == TV and order['orderDay'] == 21:
           counterTV += order['orderPiece']

    return f"A rendelt termékek darabszáma a 21. napon: PL: {counterPL}, TV: {counterTV}, NR: {counterNR} "  

exerciseSeven = exerciseSeven()
print(exerciseSeven)

def exerciseEight(): #Még nincs kész
   counterPL = 0
   counterNR = 0
   counterTV = 0
   counterPL2 = 0
   counterNR2 = 0
   counterTV2 = 0
   counterPL3 = 0
   counterNR3 = 0
   counterTV3 = 0

   for order in orders:
       if order['orderDay'] < 11:
           if order['orderCity'] == "PL":
            counterPL += order['orderPiece']
           if order['orderCity'] == "NR":
            counterNR += order['orderPiece']
           if order['orderCity'] == "TV":
            counterTV += order['orderPiece']
       elif 10 < order['orderDay'] < 21:
            if order['orderCity'] == "PL":
             counterPL2 += order['orderPiece']
            if order['orderCity'] == "NR":
             counterNR2 += order['orderPiece']
            if order['orderCity'] == "TV":
             counterTV2 += order['orderPiece']
       elif 20 < order['orderDay'] < 31:
            if order['orderCity'] == "PL":
             counterPL3 += order['orderPiece']
            if order['orderCity'] == "NR":
             counterNR3 += order['orderPiece']
            if order['orderCity'] == "TV":
             counterTV3 += order['orderPiece']

       #print(counterPL)
           

exerciseEight = exerciseEight()
print(exerciseEight)