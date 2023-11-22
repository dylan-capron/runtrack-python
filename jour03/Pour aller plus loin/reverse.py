def inverse_string(chaine):
    return chaine[::-1]
chaine_originale = input("Entrez le mot : ")
chaine_inverse = inverse_string(chaine_originale)
print(f"Chaine originale : {chaine_originale}")
print(f"Chaine inversée : {chaine_inverse}")
