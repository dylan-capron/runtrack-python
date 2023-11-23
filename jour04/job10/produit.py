def calculproduit(liste, borne_inf, borne_sup):
    produit = 1
    for valeur in liste:
        if borne_inf <= valeur <= borne_sup:
            produit *= valeur
    return produit
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
borne_inf = 25
borne_sup = 90
produit = calculproduit(L, borne_inf, borne_sup)
print(f"Le produit des valeurs comprises dans l'intervalle [{borne_inf}, {borne_sup}] est :", produit)
