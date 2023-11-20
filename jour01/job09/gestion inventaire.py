nom_du_produit = "Télévision"
prix_unitaire = 400.0
quantité_stock = 60
print (f"Nom du produit: {nom_du_produit} \n Prix: {prix_unitaire} \n Quantité: {quantité_stock}")
quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock : "))
quantité_stock += quantite_ajoutee
prix_unitaire *= 1.1
print("\nInformations mises à jour du produit après ajout en stock et augmentation de prix :")
print(f"Nom du produit : {nom_du_produit}")
print(f"Prix unitaire : {prix_unitaire:.2f} euros") 
print(f"Quantité: {quantité_stock}")