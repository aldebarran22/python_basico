"""
Leer de teclado en Python
"""

# Leer de teclado y convertir a número entero:
importe = int(input("Teclear importe:"))
if importe % 10 == 0:
    # Comprobar que el importe es múltiplo de 10
    tipoBillete = int(input("Teclear tipo de billetes:"))
    numBilletes = importe // tipoBillete
    resto = importe % tipoBillete
    print("número de billetes: ", numBilletes, "resto", resto)
else:
    print('No es correcto el importe')


if importe % 10 == 0:
    pass

