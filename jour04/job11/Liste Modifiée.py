def augmentation(liste):
    nouvelle_liste = [element + 1 for element in liste]
    return nouvelle_liste
L = [7, 11, 42, 39, 2]
L_modifiee = augmentation(L)
print(L)
print(L_modifiee)
