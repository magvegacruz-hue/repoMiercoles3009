print("Bienvenido")
print("Inserte los digitos de una matriz 2x2")
matrizC = []
for fila in range(2):
    matrizC.append([])
    for columna in range(2):
        valor = int(input(f"Fila {fila+1}, columna {columna+1}: "))
        matrizC[fila].append(valor)

for fila in matrizC:
    print(fila)
k = int(input("Ahora dime el escalar para multiplicar a la matriz: "))

matrizB = []
for i in range(len(matrizC)):
    matrizB.append([])
    for j in range(len(matrizC)):
        matrizB[i].append(k * matrizC[i][j])

print("="*13)
print("Escalar", k)
for fila in matrizB:
    print(fila)