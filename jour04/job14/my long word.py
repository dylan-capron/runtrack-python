def my_long_word(longueur_minimale, chaine):
    mots_plus_longs = []
    mot_en_cours = ""
    resultat_temporaire = []

    for caractere in chaine:
        if caractere == " " or caractere == "," or caractere == ".":
            longueur_mot = 0
            for _ in mot_en_cours:
                longueur_mot += 1
            if longueur_mot > longueur_minimale:
                resultat_temporaire = resultat_temporaire + [mot_en_cours]
            mot_en_cours = ""
        else:
            mot_en_cours += caractere
    longueur_mot = 0
    for _ in mot_en_cours:
        longueur_mot += 1
    if longueur_mot > longueur_minimale:
        resultat_temporaire = resultat_temporaire + [mot_en_cours]

    mots_plus_longs.extend(resultat_temporaire)

    return mots_plus_longs
longueur_minimale = 3
chaine_test = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(longueur_minimale, chaine_test)
print(f"Mots de plus de {longueur_minimale} caractères dans la chaîne : {resultat}")
