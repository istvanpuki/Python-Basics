print("Add meg a fizetésed összegét Forintban!")

def fizetes(illetmeny):
    illetmeny = float(illetmeny)
    illetmeny = round(illetmeny)
    
    if illetmeny >= 200000:
        print()    
        print(f"Sajnos nem tudom megemelni a {illetmeny} Ft. összegű fizetésed.")

        #tagolt_illetmeny =  "{:,}".format(illetmeny)
        #print(f"Sajnos nem tudom megemelni a {tagolt_illetmeny} Ft. összegű fizetésed.")

    else:
        emelt_illetmeny = round(illetmeny * 1.20)
        print()
        print(f"Az a jó hírem van, hogy 20%-al megemelem a fizetésedet, így {emelt_illetmeny} Ft. lesz a fizetésed")

        #tagolt_emelt_illetmeny = "{:,}".format(emelt_illetmeny)
        #print(f"Az a jó hírem van, hogy 20%-al megemelem a fizetésedet, így {tagolt_emelt_illetmeny} Ft. lesz a fizetésed")

fizetes(input())