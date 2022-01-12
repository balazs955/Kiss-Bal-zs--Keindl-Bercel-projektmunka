import random

jatek = input("Válassz (kő, papír, olló): ")
possible_actions = ["kő", "papír", "olló"]
computer_action = random.choice(possible_actions)
print(f"\nVálassz {jatek}, Gép választás {computer_action}.\n")

if jatek == computer_action:
    print(f"Döntetlen {jatek}.!")

elif jatek == "kő":
    if computer_action == "olló":
        print("Nyertél!")
    
    else:
        print("A papír erősebb mint a kő! Vesztettél.")

elif jatek == "papír":
    if computer_action == "kő":
        print("Nyertél!")
    
    else:
        print("olló erősebb mint a papír! Vesztettél.")

elif jatek == "olló":
    if computer_action == "papír":
        print("Nyertél!")
    
    else:
        print("A kő erősebb mint a olló! vesztettél.")