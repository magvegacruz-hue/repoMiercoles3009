"""
Dada una matriz cuadrada, convertirla en matriz identidad
"""
matrizA = []
dimension = int(input("dimensiones de la matriz cuadrada: "))
for i in range(dimension):
    matrizA.append([])
    for j in range(dimension):
        matrizA[i].append(int(input(f"fila {i+1}, columna {j+1}: ")))
print("="*13)
print("Matriz A")
#identidad 
for i in range(len(matrizA)):
    for j in range(len(matrizA)):
        if i == j:
            matrizA[i][j] = 1
        else:
            matrizA[i][j] = 0

for fila in matrizA:
    print(fila)
    

