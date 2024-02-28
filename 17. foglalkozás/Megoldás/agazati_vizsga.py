def exercise_one():
    print("1. feladat: Kisebb-nagyobb meghatározása")
    num_a= int( input("Kérem az első számot: ")) 
    num_b= int( input("Kérem az első számot: "))

    if num_a > num_b:
        print(f"A nagyobb szám {num_a}, a kisebb {num_b}. ")
    elif num_a == num_b:
        print("A két szám egyenlő.")
    else:
        print(f"A nagyobb szám {num_b}, a kisebb {num_a}.")
   
def exercise_two():
    leap_years = []
    print("2. feladat: Szökőév listázó")
    year_a= int( input("Kérem az egyik évszámot: ")) 
    year_b= int( input("Kérem a másik évszámot: "))

    if year_a > year_b:
        year_c = year_a
        year_a = year_b
        year_b = year_c
    
    for year in range(year_a, year_b+1):
        if year % 400 == 0:
            leap_years.append(year)
        elif year % 4 == 0 and year % 100 != 0:
            leap_years.append(year)

    if len(leap_years) == 0:  
        print("Nincs szökőév a megadott tartományban!")
    else:
        leap_years_string = "Szökőévek: "     
        for year in leap_years:
            leap_years_string += f" {year}; "

    print(leap_years_string)

def exercise_three_without_class():
    building = {}
    buildings = []

    with open('varosok.txt', 'r', encoding='UTF-8') as file:
        file.readline()
        for line in file:
            data = line.strip().split(';')

            building = {
                'name': data[0],
                'city': data[1],
                'country': data[2],
                'height': float(data[3].replace(',', '.')),
                'floor': int(data[4]),
                'madeYear': int(data[5]),
            }
            buildings.append(building)

    #print(buildings)
    print(f"3.2 feladat: Épületek száma: {len(buildings)} db")

    floors = 0
    for b in buildings:
        floors += b['floor']
    print(f"3.3. feladat: Emeletek összege {floors}")

    tallest = buildings[0]
    for b in buildings:
        if b['height'] > tallest['height']:
            tallest = b
    print('3.4 feladat: A legmagasabb épület adatai')
    print(f"\t Név: {tallest['name']}")
    print(f"\t Város: {tallest['city']}")
    print(f"\t Ország: {tallest['country']}")
    print(f"\t Magasság: {tallest['height']} m")
    print(f"\t Emeletek száma: {tallest['floor']}")
    print(f"\t Építés éve: {tallest['madeYear']}")

    olasz = False
    for b in buildings:
        if b['country'] == "Olaszország":
            olasz = True
    if olasz == True:
        print("3.5. feladat: Van olasz épület az adatok között!")
    else:
        print('3.5 feladat: Nincs olasz épület az adatok között!')    

#Exercise three class and constructor
class Building:
    name = ""
    city = ""
    country = ""
    height = 0.0
    floor = 0
    madeYear = 0

    '''
    class Building:
        def __str__(self):
            return f"{self.name} ({self.city}, {self.country}) - Magasság: {self.height} m, Emeletek: {self.floor}, Építés éve: {self.madeYear}"
    '''

    def __init__(self, row): #The row parameter is from the varosok.txt file, and the row is include the building attributes.
        rowData = row.strip().split(";")

        self.name = rowData[0]
        self.city = rowData[1]
        self.country = rowData[2]
        self.height = float( rowData[3].replace(',', '.') )
        self.floor = int( rowData[4] )
        self.madeYear = int( rowData[5] )


def exercise_three():
    buildings = [] 

    with open("varosok.txt", "r", encoding='UTF-8') as file:
        file.readline()
        for r in file:
            row = Building(r)
            buildings.append(row)
    #print(buildings) Itt wil show <__main_: object at memory address>

    print(f"3.2 feladat: Épületek száma: {len(buildings)} db")

    floors = 0
    for b in buildings:
        floors += b.floor
    print(f"3.3. feladat: Emeletek összege {floors}")

    tallest = buildings[0]
    for b in buildings:
        if b.height > tallest.height:
            tallest = b
    print('3.4 feladat: A legmagasabb épület adatai')
    print(f"\t Név: {tallest.name}")
    print(f"\t Város: {tallest.city}")
    print(f"\t Ország: {tallest.country}")
    print(f"\t Magasság: {tallest.height} m")
    print(f"\t Emeletek száma: {tallest.floor}")
    print(f"\t Építés éve: {tallest.madeYear}")

    italian = False
    for b in buildings:
        if b.country == "Olaszország":
            italian = True
    if italian == True:
        print("3.5. feladat: Van olasz épület az adatok között!")
    else:
        print('3.5 feladat: Nincs olasz épület az adatok között!')  
exercise_one()
exercise_two()
#exercise_three_without_class()
exercise_three()
