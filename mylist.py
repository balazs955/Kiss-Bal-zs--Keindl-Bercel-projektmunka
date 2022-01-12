from random import randint

jatek = ["kő", "papír", "olló"]

gep = jatek[randint(0,2)]

jatekos = False

while jatekos == False:

    jatekos = input("kő, papír, olló")
    
    if jatekos == gep:
        print("Döntetlen!")
   
    elif jatekos == "kő":
        
        if jatekos == "Papír":
            print("Vesztettél!", gep, "erősebb mint a(z)", jatekos)
        else:
            print("Nyertél!", jatekos, "erősebb mint a(z)", gep)
    
    elif jatekos == "papír":
        
        if gep == "olló":
            print("Vesztettél!", gep, "erősebb mint a(z)", jatekos)
        else:
            print("Nyertél!", jatekos, "erősebb mint a(z)", gep)
    
    elif jatekos == "olló":
        
        if gep == "kő":
            print("Vesztettél", gep, "erősebb mint a(z)", jatekos)
        else:
            print("Nyertél!", jatekos, "erősebb mint a(z)", gep)
   
    else:
        print("rosszul írtad be. írd be újra!")
    
    jatekos = False
    gep = jatek[randint(0,2)]