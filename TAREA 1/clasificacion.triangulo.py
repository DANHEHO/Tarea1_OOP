def triangulo(base, l1, l2):

    if base <= 0 or l1 <= 0 or l2 <= 0:
        return "Error: Los lados deben ser mayores a cero."
    
    if (base + l1 <= l2) or (base + l2 <= l1) or (l1 + l2 <= base):
        return "Error: Los lados no forman un triángulo válido."
    
    if base == l1 == l2:
        return "El triángulo es equilátero."
    elif base == l1 or base == l2 or l1 == l2:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."

base = float(input("Ingresa la base del triángulo: "))
l1 = float(input("Ingresa un lado del triángulo: "))
l2 = float(input("Ingresa el otro lado del triángulo: "))

print(triangulo(base, l1, l2))