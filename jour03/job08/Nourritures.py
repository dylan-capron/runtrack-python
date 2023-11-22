def Nourritures(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
        else:
            print("Saison Inconnue")
    elif type == "legume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "ete":
            print("Artichaut, aubergine, navet")
        else:
            print("Saison Inconnue")
    else:
        print("Type Inconnue")

Nourritures("fruits", "hiver")
Nourritures("fruits", "ete")
Nourritures("legume", "hiver")
Nourritures("legume", "ete")
Nourritures("poisson", "automne")