# PROYECTO #3
# ANDY ALEXIS CABRERA TORRES
# En este proyecto voy a realizar un simulador de factura en donde se calculara subtotal junto con el respectivo IVA
from pydoc import describe

print ("----- SIMULADOR DE FACTURA -----")
cliente = input("Nombre del cliente")
producto = input("¿Que producto compro?")
cantidad = int(input("Cantidad de producto comprado"))
precio_unitario = int(input("Precio del producto"))
# Declaramos el subtotal
subtotal = cantidad*precio_unitario
if (subtotal > 100):
    print("Felicidades obtuvo un descuento del 20%")
    descuento = subtotal * 0.20
else:
    descuento = 0
sub_total_con_descuento = subtotal - descuento
iva = subtotal * 0.15
total_pagar = sub_total_con_descuento + iva

print("\n" + "="*30)
print(f"FACTURA COMERCIAL")
print(f"Cliente: {cliente}")
print(f"Producto: {producto} (x{cantidad})")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: -${descuento:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"TOTAL A PAGAR: ${total_pagar:.2f}")
print("="*30)

