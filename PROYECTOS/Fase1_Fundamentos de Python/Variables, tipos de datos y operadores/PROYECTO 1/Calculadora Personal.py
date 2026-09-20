# Este es mi primer programa en Python el cual consiste en una calculadora simple de operaciones basicas
# PROYECTO #1
# ANDY ALEXIS CABRERA TORRES
print (f"-----Bienvenido a la calculora-----")
print (f"Ingrese la operación que desea realizar")
print (f"1-SUMA\n 2-RESTA\n 3-MULTIPLICACIÓN\n 4-DIVISIÓN")
operacion = int(input("Ingrese la operación que desea realizar"))
if operacion == 1:
    num1= float(input("Ingrese el primer numero"))
    num2 = float(input("Ingrese el segundo numero"))
    suma = num1 + num2
    print(suma)
if operacion == 2:
    num1 = float(input("Ingrese el primer numero"))
    num2 = float(input("Ingrese el segundo numero"))
    resta = num1 - num2
    print(resta)
if operacion == 3:
    num1 = float(input("Ingrese el primer numero"))
    num2 = float(input("Ingrese el segundo numero"))
    multiplicación = num1 * num2
    print(multiplicación)
if operacion == 4:
    num1 = float(input("Ingrese el primer numero"))
    num2 = float(input("Ingrese el segundo numero"))
    if num2 == 0:
        print("Número no válido, no se puede dividir entre cero.")
    else:
        división = num1 / num2
        print(f"El resultado es: {división}")
