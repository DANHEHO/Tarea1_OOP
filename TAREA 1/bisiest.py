"""Año bisiesto
Solicita un año e indica si es bisiesto o no.
(Un año es bisiesto si es divisible entre 
4 pero no entre 100, o si es divisible entre 400)."""

def es_bisiesto(anio):
  if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    return True
  else:
    False
  
try:
  anio = int(input("Ingresa un ano: "))

  if es_bisiesto(anio):
    print(f"El ano {anio} es bisiesto.")
  else:
    print(f"El ano {anio} no es bisiesto")

except ValueError:
  print("Por favor, ingresa un numero valido.")