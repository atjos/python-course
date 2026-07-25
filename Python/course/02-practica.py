check_number = int(input("Coloque el número entero a verificar: "))

if check_number % 2 == 0:
    print("Su candidato es un número primo.")
else:
    print("No es un número primo.")

print(type("10"))
print(type(10))

number = int(float('9.8'))
print(number)

# CALCULAR PAGO SEMANAL

horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas por semana: "))
pago_hora = float(input("Ingrese el pago por hora: "))

pago_semanal = float(horas_trabajadas * pago_hora)

print(f"Su pago es: {pago_semanal}")

años_vividos = int(float(input("Enter number of years you have lived: ")))
segundos_año = 31557600
segundos_vividos = int(años_vividos * segundos_año)

print(f"Ha vivido {segundos_vividos} segundos.")