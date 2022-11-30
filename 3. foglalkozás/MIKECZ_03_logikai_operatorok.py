#Logikai operátorok - And Or Not
#and (és)
#or (vagy)
#not (tagadás)

szam1 = 2
szam2 = 4

#           True           True
print(szam1 < szam2 and szam1 == 2)
#           True             False
print(szam1 < szam2 and szam1 == 3)
#           True           False
print(szam1 < szam2 or szam1 == 3)

print(szam1 < szam2 and not szam1 == 3) #and not false a jelentése = tehát true
"""
True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or Fale = False

True and not false = True
"""

