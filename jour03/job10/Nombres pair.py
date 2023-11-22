def verifie_pair_impair(n):
    if isinstance(n, int) and n >= 0:
        if n % 2 == 0:
            return "Pair"
        else:
            return "Impair"
    else:
        return "Veuillez entrer un nombre entier positif."
resultat1 = verifie_pair_impair(8)
resultat2 = verifie_pair_impair(15)
resultat3 = verifie_pair_impair(-3)
resultat4 = verifie_pair_impair("abc")
print(f"8 est {resultat1}")
print(f"15 est {resultat2}")
print(f"-3 est {resultat3}")