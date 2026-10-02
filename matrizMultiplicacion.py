from ingresarMatrices import ingresarMatrizA, ingresarMatrizB
#Multiplicacion de matrices
def multiplicarMatrices():
    matrizC = []
    matrizA, dimension = ingresarMatrizA()
    matrizB = ingresarMatrizB(dimension)
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            suma = 0
            for k in range(dimension):
                suma += matrizA[i][k] * matrizB[k][j]
            fila.append(suma)
        matrizC.append(fila)
        #Mostrar matrices
    print("La matriz resultante es:")
    for fila in matrizC:
        print(fila)
