import random

jatekos = int(0)
gep = int(0)
pontszam = 5


while jatekos != pontszam or gep != pontszam:

    jatekos_valasztas: str = input(str("kő papír olló:")).lower()

    jatek = "kő", "papír", "olló"
    gep_valasztas = random.choice(jatek)
    print("A gép választása:")

    if gep_valasztas == "kő" and jatekos_valasztas == "kő":
        print ( "döntetlen" )

    if gep_valasztas == "papír" and jatekos_valasztas == "papír":
        print ( "döntetlen" )

    if gep_valasztas == "olló" and jatekos_valasztas == "olló":
        print ( "döntetlen" )

    if gep_valasztas == "papír" and jatekos_valasztas == "kő":
        print ( "a gép szerzett pontot" )

        gep = gep + 1
        print ( "a gép pontszáma:", gep )

    if gep_valasztas == "kő" and jatekos_valasztas == "papír":
        print ( "Nyertél" )

        jatekos = jatekos + 1
        print ( "a pontszámod:", jatekos )

    if gep_valasztas == "kő" and jatekos_valasztas == "olló":
        print ( "a gép szerzett pontot" )

        gep = int ( gep ) + 1
        print ( "a gép pontszáma:", gep )

    if gep_valasztas == "olló" and jatekos_valasztas == "kő":
        print ( "Nyertél" )

        jatekos = jatekos + 1
        print ( "a pontszámod:", jatekos )

    if gep_valasztas == "papír" and jatekos_valasztas == "olló":
        print ( "Nyertél" )

        jatekos = jatekos + 1
        print ( "a pontszámod:", jatekos )

    if gep_valasztas == "olló" and jatekos_valasztas == "papír":
        print ( "a gép szerzett pontot" )

        gep = int ( gep ) + 1
        print ( "a gép pontszáma", gep )

        gep_valasztas = random.choice ( jatek )

        if jatekos == pontszam:
            print("Gratulálok Nyertél")

        elif gep == pontszam:
            print("Sajnálom vesztettél próbáld meg újra.")

        break