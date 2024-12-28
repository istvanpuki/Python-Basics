import auto

carsInformations = []

with open("jeladas.txt", "r", encoding="UTF-8") as file:
    for line in file:
        carInfo = auto.Auto(line) # from auto modul We use Auto Class
        carsInformations.append(carInfo)

print(carsInformations) # It wil show <__main_: object at memory address>