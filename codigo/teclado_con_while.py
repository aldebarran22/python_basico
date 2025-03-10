"""
Leer de teclado en Python

while True:
    1) lectura del importe (validando)
    2) desglosar el importe en billetes
"""

billetes = [50, 20, 10]
while True:
    # 1) Lectura de teclado con validación
    print('\nRETIRADA DE EFECTIVO:')
    importe = 1
    while importe % 10 != 0:
        importe = int(input("Teclear importe:"))
        if importe % 10 != 0:
            print('Importe no válido, necesitamos un múltiplo de 10')

    # 1 bis) Lectura con bucle infinito, y rompemos el bucle con break
    """
    while True:
        importe = int(input("Teclear importe:"))
        if importe % 10 != 0:
            print('Importe no válido, necesitamos un múltiplo de 10')
        else:
            break
    """

    # 2) Desglosar el importe en billetes:    
    for tipoBillete in billetes:
        if importe >= tipoBillete:
            numBilletes = importe // tipoBillete        
            importe = importe % tipoBillete # importe %= tipoBillete
            print("número de billetes de ",tipoBillete,"=", numBilletes)



