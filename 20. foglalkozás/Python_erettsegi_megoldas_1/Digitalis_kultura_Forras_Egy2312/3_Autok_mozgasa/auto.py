class Auto:

    rendszam : str          # Kevésbé elegánsan: rendszam = ""
    ora : int               # Kevésbé elegánsan: ora = 0
    perc : int             # Kevésbé elegánsan: perc = 0
    sebesseg : int            # Kevésbé elegánsan: sebesseg = 0

    def __init__(self, line):
        
        data = line.strip().split()

        self.rendszam = data[0]
        self.ora = int(data[1])
        self.perc = int(data[2])
        self.sebesseg = int(data[3])