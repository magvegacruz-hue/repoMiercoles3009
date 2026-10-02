def ingresarMatrizA():
    matrizA = []
    
    while True:
        try:
            print("Inserte la cantidad de dimensiones de la matriz nxn: ", end="")
            dimension = int(input())
            if dimension > 0:
                break
            else:
                print("Debe ser mayor a 0")
        except ValueError:
                print("Debe insertar un numero entero")

    for fila in range(dimension):
        matrizA.append([])
        for columna in range(dimension):
            while True:
                try:
                    valor = int(input(f"Fila {fila+1}, columna {columna+1}: "))
                    matrizA[fila].append(valor)
                    break
                except ValueError:
                    print("Debe insertar un numero")

    for fila in matrizA:
        print(fila)
    print("="*13)
    return matrizA, dimension

def ingresarMatrizB(dimension):
    print(f"Inserte los digitos de otra matriz {dimension}x{dimension}: ")
#segunda matriz
    matrizB = []
    for fila in range(dimension):
        matrizB.append([])
        for columna in range(dimension):
            while True:
                try:
                    valor = int(input(f"Fila {fila+1}, columna {columna+1}: "))
                    matrizB[fila].append(valor)
                    break
                except ValueError:
                    print("Debe ser un numero")

    for fila in matrizB:
        print(fila)
    print("="*13)
    return matrizB