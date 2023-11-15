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
    searchMax = []
    biggestPiece = 0
    orderDay = []
    correctDay = 0
    for order in orders:
        searchMax.append(order['orderPiece'])
    biggestPiece = max(searchMax)

    for order in orders:
        if order['orderPiece'] == 9:
            orderDay.append(order['orderDay'])
    correctDay = orderDay[0]        
    return f"A legnagyobb darabszám: {biggestPiece}, a rendelés napja: {correctDay}" 

print("5. feladat: ")
maxpiece = maxPiece()
print(f"{maxpiece}")

# Exercise 6. nincs kész

def osszes(orderDay, orderCity):
    day = orderDay
    cityName = orderCity
    counter = 0
    for order in orders:
        if day == order['orderDay'] and cityName == order['orderCity']:
            counter = counter + order['orderPiece']
    return counter

osszes = osszes( str( input("OrderCity: ") ), int( input("OrderDay: ") ) )
print(osszes)