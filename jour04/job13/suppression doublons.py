def doublons(liste):
    liste_unique = []
    for element in liste:
        if element not in liste_unique:
            liste_unique.append(element)
    return liste_unique
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = doublons(ma_liste)
print("Liste sans doublons :", liste_sans_doublons)
