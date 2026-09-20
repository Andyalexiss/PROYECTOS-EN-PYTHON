# PROYECTO #2
# ANDY ALEXIS CABRERA TORRES
# En este proyecto vamos a trabajar en un conversor de unidades, usando la estrcutura match. Vamos a trabajar con 4 casos

#Parte de ingreso de datos
print ("----- BIENVENIDO AL CONVERSOR DE UNIDADES -----")
print ("1- De Grados a Farenheit")
print ("2- De Metro a Kilometro")
print ("3- De Centimetro a Metro")
print ("4- De Milimetro a Centimetro")
opcion = int(input(" Ingrese su opción"))
match(opcion):
    case 1:
        G = float(input("Ingrese los Grados"))
        F = G * 9/5 + 32
        print(f"Esta es la temperatura en Farenheit {F}")
    case 2:
        M = float(input("Ingrese los Metros"))
        KM = M/1000
        print(f"{M} metros en kilometros son: {KM}")
    case 3:
        CM = float(input("Ingrese los Centimetros"))
        M= CM / 100
        print(f"{CM} centimetros en metros son: {M}")
    case 4:
        MM = float(input("Ingrese los Milimetros"))
        CM = MM / 10
        print(f"{MM} milimetros en centimetros son: {CM}")
    case _:
        print("Opcioón no valioda")

