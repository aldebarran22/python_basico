"""
Prueba con las listas de Python
"""

L = [12,33,11,11,44,55]
print(L)
L[5] = 10
print(L, type(L))
print('Recuento: ', len(L))
print('Suma: ', sum(L))
print('minimo: ', min(L))
print('maximo: ', max(L))
print('promedio: ', sum(L)/len(L))

print('hola tiene', len("hola"), "letras")

# Posible aplicación de un índice negativo de una lista
path = "D:/OneDrive/Escritorio/python_basico/codigo/listas.xlsx"
L = path.split("/")
print(L[-1])

# Recorrer una lista con un bucle:
billetes = [50, 20, 10]
for tipoBillete in billetes:
    print(tipoBillete)




