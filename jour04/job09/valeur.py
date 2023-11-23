def MinMax ():
    valeur = L[0]
    valeur_minimale = min(L)
    valeur_maximale = max(L)
    return valeur, valeur_minimale, valeur_maximale
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
valeur, valeur_minimale, valeur_maximale = MinMax ()
print("Valeur de l'élément à l'index 0 :", valeur)
print("Valeur minimale de la liste :", valeur_minimale)
print("Valeur maximale de la liste :", valeur_maximale)
MinMax ()