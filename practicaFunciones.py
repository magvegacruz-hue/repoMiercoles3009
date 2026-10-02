nombre = input("nombre: ")
def saludar(nombre):
    print(f"hola, {nombre}")
saludar(nombre)

a = int(input("a: "))
b = int(input("b: "))
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(a, b)
print(f"el total es: {total}")

def sumaConPrint():
    resultado = a + b
    return resultado

sumaConPrint()