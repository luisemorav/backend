# Crear un programa que te permita ingresar 6 numeros de los cuales, si uno no fuera un numero, indicara un mensaje de error
# pero los que si tengan un formato correcto se agregaran a una lista

numeros = []

for _ in range(6):
    try:
        numero = int(input('Ingresa un numero: '))
        numeros.append(numero)
    except Exception:
        print('El número ingresado es incorrecto')

print(numeros)
