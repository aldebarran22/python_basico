"""
Operaciones aritméticas entre variables y contantes
"""

# Calcular el IVA de un producto:
precio = 125
iva = 21

valorIva = precio * (iva / 100)
total = precio + valorIva
print('precio',precio,'iva',iva,'valor iva', valorIva)
print('total', total)

# Calcular media de dos números
num1 = 34
num2 = 67
media = (num1 + num2) / 2
print("media: ", media)

# Número de billetes de 50 para 230 eur
importe = 230 
numBilletes = importe // 50
resto = importe % 50
print('número de billetes: ', numBilletes, "resto",resto)

# Potencia:
print('2 elevado a 10', 2**10)

# Decimales
print(0.1 + 0.2)
print(round(0.1+0.2, 2))
print(round(0.1+0.2))

