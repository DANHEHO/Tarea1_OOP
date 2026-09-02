"""Solicita la edad de una persona y muestra el costo de 
entrada a un parque:
Menores de 12 años: $50
De 12 a 17 años: $80
Adultos (18 en adelante): $120"""

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    costo = 50
elif edad <= 17:
    costo = 80
else:
    costo = 120

print(f"El costo de entrada es: ${costo}")