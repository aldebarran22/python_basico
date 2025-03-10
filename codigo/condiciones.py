"""
Condiciones, operadores relacionales (==, >, >=, <, <=, !=)
 - lógicos (and, or, not)
"""

# Comprobar si una variable está dentro de un rango:
ini = 5
fin = 15
numero = 13
if numero >= ini and numero <= fin:
    print("dentro del rango")
else:
    print("fuera del rango")

# Lo mismo pero con una sintaxis propia de python:
if ini <= numero <= fin:
    print("dentro del rango")
else:
    print("fuera del rango")

if not (ini <= numero <= fin):
    print("fuera del rango")
else:
    print("dentro del rango")

if numero < ini or numero > fin:
    print("fuera del rango")
else:
    print("dentro del rango")

# Cual es el menor de dos numeros, controlar si son iguales:
if ini < fin:
    print("el menor es:", ini)
elif ini == fin:
    print("Son iguales")
else:
    print("El menor es:", fin)

ini = 20
fin = 10
menor = ini if ini < fin else fin if fin < ini else "iguales"
print('menor: ', menor)
#exit()

# Forma comprimida:
print("par" if numero % 2 == 0 else "impar")

# Forma: if else
if numero % 2 == 0:
    print("par")
else:
    print("impar")

# Imprimir el binario, octal y hexadecimal:
numero = 19
print(numero)
print(bin(numero))
print(oct(numero))
print(hex(numero))
