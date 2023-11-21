N = int(input("N : "))
print (N)
if N > 0:
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i} :")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} x {j} = {produit}")