"""
Dada una matriz de identidad nxn 
mostrar en color azul solo la capial de 1
"""
matrizA = []

dimension = int(input("dimensiones de la matriz identidad: "))
for i in range(dimension):
    fila = []
    for j in range(dimension):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matrizA.append(fila)

from colorama import Fore, Style

for i in range(dimension):
    for j in range(dimension):
        if i == j:
            print(Fore.BLUE + str(matrizA[i][j]) + Style.RESET_ALL, end=" ")
        else:
            print(matrizA[i][j], end=" ")
    print()
