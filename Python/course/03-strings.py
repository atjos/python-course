### STRINGS ###

oración_larga = '''I am a teacher and enjoy teaching. 
I didn't find anything as rewarding as empowering people. 
That is why I created 30 days of python.'''

print(oración_larga)

mensaje = "Hola J Juan José"
adición = input("Agregue lo que sea: ")
mensaje += adición
print(mensaje)

# TIP, para evadir tener que convertir un int a str a la hora de concatenar es mejor hacer uso de ',' en vez de '+'

number_one = 2
number_two = 4
resultado = str(number_one + number_two)

print("El resultado de su operación es: " + resultado)

# EMPIEZA A CONTAR DESDE EL 0 LA FUNCIÓN 'FIND'

buscar_subcadena = mensaje.find("Juan")
print(buscar_subcadena)

extrae_cadena = mensaje[0:4]
print(extrae_cadena)
