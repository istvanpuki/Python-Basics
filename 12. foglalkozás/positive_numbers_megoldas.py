'''
Feladat:
Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap három számot és
eldönti, hogy az összes paramétere pozitív-e! A programodban hívd is meg ezt az alprogramot!

'''

print('Adj meg három számot:')

def pos_numbers(num1, num2, num3):
    if num1 > 0 and num2 > 0 and num3 > 0:
        return True
    else:
        return False

output = pos_numbers(int(input()), int(input()), int(input()))
print(output)