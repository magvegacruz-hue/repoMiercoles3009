from ingresarMatrices import ingresarMatrizA, ingresarMatrizB
#suma de matrices
def restarMatrices():
    matrizC = []
    matrizA, dimension = ingresarMatrizA()
    matrizB = ingresarMatrizB(dimension)
    for i in range(dimension):
        matrizC.append([])
        for j in range(dimension):
            matrizC[i].append(matrizA[i][j] - matrizB[i][j])
    print("="*13)
    print("Matriz A-B: ")
    for fila in matrizC:
        print(fila)