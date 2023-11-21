a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Équilatéral"
        elif a == b or a == c or b == c:
            return "Isocèle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Rectangle"
        else:
            return "Quelconque"
    else:
        return "Impossible de construire un triangle"

resultat = type_triangle(a, b, c)
print(f"Le triangle est {resultat}.")
