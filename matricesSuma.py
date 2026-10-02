
print("="*13)
print("Bienvenido")
print("="*13)
print("Inserte los digitos de una matriz 3x3")
#primera matriz
matrizA = []
for fila in range(3):
    matrizA.append([])
    for columna in range(3):
        valor = int(input(f"Fila {fila+1}, columna {columna+1}: "))
        matrizA[fila].append(valor)

for fila in matrizA:
    print(fila)
print("="*13)
print("Inserte los digitos de otra matriz 3x3")
#segunda matriz
matrizB = []
for fila in range(3):
    matrizB.append([])
    for columna in range(3):
        valor = int(input(f"Fila {fila+1}, columna {columna+1}: "))
        matrizB[fila].append(valor)
for fila in matrizB:
    print(fila)
print("="*13)
#suma de matrices
matrizC = []
for i in range(len(matrizA)):
    matrizC.append([])
    for j in range(len(matrizA)):
        matrizC[i].append(matrizA[i][j] + matrizB[i][j])
print("="*13)
print("Matriz A+B: ")
for fila in matrizC:
    print(fila)