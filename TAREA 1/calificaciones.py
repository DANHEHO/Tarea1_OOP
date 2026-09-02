"""Pide una calificación numérica (0–100) y
 muestra la equivalencia en letra:
90–100: A
80–89: B
70–79: C
60–69: D
Menor a 60: F"""

calificacion = float(input("Ingresa la calificación numérica (0-100): "))

if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"

print(f"Equivalencia en letra: {letra}")