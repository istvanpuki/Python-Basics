class Ingatlan:
    def __init__(self, cím, négyzetméter, ár):
        self.cím = cím
        self.négyzetméter = négyzetméter
        self.ár = ár
        
    
    def négyzetméterÁr(self):
        return round(self.ár / self.négyzetméter) 

Ház1 =Ingatlan("Nyh", 66, 10000000)
print(Ház1)
print(Ház1.cím)
print(Ház1.négyzetméterÁr())

Ház2 =Ingatlan("Deb", 72, 20000000)
print(Ház2)
print(Ház2.cím)
print(Ház2.négyzetméterÁr())