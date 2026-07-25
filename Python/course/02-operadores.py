### Operadores Aritméticos###

print(5 + 5)
print(5 - 12)
print(5 * 10)
print(5 / 8)
print(10 % 3)  # Módulo - Resto de una división
print(2 ** 3)
print(10 // 3)  # División entera - Parte entera de una división

float = 3.7 * 2
# Repetición de cadenas usando la función int() para convertir float a entero
print("Hola " * int(float))

# Operadores de comparación

print(8 > 3)
print(5 < 2)
print(10 >= 10)
print(4 <= 1)
print(7 == 7)
print(3 != 5)

print("Hola" > "Python")

edad_usuario = 19
verificación_edad = 20
acceso = edad_usuario >= verificación_edad
print("¿El usuario tiene acceso?", acceso)

# Calculadora

price = 2000
products = 3
total = price * products
iva = total * 0.19
final_price = total + iva
print("El precio total es:", final_price)

# Operadores Lógicos

age = 18
has_license = True

if age > 19 and has_license is True:
    print("Está apto para conducir")
else:
    print("No está apto para conducir")

# Queremos verificar si una persona puede conducir un vehículo en la ciudad de Bucaramanga

age = 19
has_license = True
borracho = False

if age >= 18 and has_license is True and borracho is False:
    print("Puede conducir")
else:
    print("No puede conducir el vehículo")

# Operadores de asignación

primer_producto = 40000
segundo_producto = 35000
tercer_producto = 40000

if primer_producto >= 50000 and segundo_producto >= 50000 and tercer_producto <= 50000:
    primer_producto *= 0.7
    segundo_producto *= 0.7
    print("El total de su compra es:", primer_producto + segundo_producto)
else:
    print("El total de su compra es:", primer_producto +
        segundo_producto + tercer_producto)



