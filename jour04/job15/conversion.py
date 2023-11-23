def tri_et_arrondi_liste(liste):
    liste_arrondie = [int(nombre + 0.5) for nombre in liste]
    n = len(liste_arrondie)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if liste_arrondie[j] > liste_arrondie[j + 1]:
                liste_arrondie[j], liste_arrondie[j + 1] = liste_arrondie[j + 1], liste_arrondie[j]
    return liste_arrondie
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = tri_et_arrondi_liste(ma_liste)
print(resultat)
