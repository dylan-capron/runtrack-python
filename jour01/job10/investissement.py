montant_initial = float(input("Entrez le montant initial de l'investissement : "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel en pourcentage : "))
gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Montant initial de l'investissement : {montant_initial} euros")
print(f"Taux de rendement annuel : {taux_rendement_annuel}%")
print(f"Gain annuel : {gain_annuel:.2f} euros")
augmentation_capital = 5000
montant_initial += augmentation_capital
augmentation_taux = 2
taux_rendement_annuel += augmentation_taux
nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print("\nInformations après augmentation du capital et du taux de rendement :")
print(f"Montant initial de l'investissement : {montant_initial} euros")
print(f"Taux de rendement annuel : {taux_rendement_annuel}%")
print(f"Nouveau gain annuel : {nouveau_gain_annuel:.2f} euros")
retrait = 0.1 * montant_initial
montant_initial -= retrait
diminution_taux = 1
taux_rendement_annuel -= diminution_taux
montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
print("\nInformations après retrait et diminution du rendement :")
print(f"Montant final de l'investissement : {montant_final:.2f} euros")
print(f"Taux de rendement annuel : {taux_rendement_annuel}%")