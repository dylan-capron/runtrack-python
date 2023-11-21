l = "abcdefghijklmnopqrstuvwxyz"

def afficher_pyramide(chaine):
    longueur = len(chaine)
    
    for i in range(0, longueur +1 -0):
        if i <= longueur:
            print(l[:i].ljust(longueur+ 4 -2))
        else:
            print(l[:longueur+3 -i])
            
afficher_pyramide(l)