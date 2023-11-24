def my_sort(input_list):
    sorted_list = list(input_list)  # Crée une copie de la liste d'entrée pour éviter de la modifier directement
    total_coups = 0  # Initialise le nombre total de coups à zéro
    n = len(sorted_list)
    tri_effectue = False  # Indicateur pour savoir si le tri est effectué
    while not tri_effectue:
        tri_effectue = True  # Admettons que la liste est triée
        # Pour parcourir la liste
        for i in range(n - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                # Échange les éléments adjacents s'ils ne sont pas dans l'ordre
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                total_coups += 1  # Augmente le nombre total de coups
                tri_effectue = False  # La liste n'est pas encore triée
    # Affiche le nombre total de coups nécessaires pour trier la liste
    print("Nombre total de coups nécessaires pour trier la liste :", total_coups)
    return sorted_list  # Permet de retourner la liste triée
# Exemple
ma_liste = [4, 2, 7, 1, 9, 5]
liste_triee = my_sort(ma_liste)
print("Liste triée :", liste_triee)
