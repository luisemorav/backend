
#TODO Ejercicio 1

# altura = int(input('Ingresa una altura: '))
# ancho = int(input('Ingresa un ancho: '))

# def dibujarRectagulo(altura, ancho):
#     for paso in range(altura):
#         print("*" * ancho)
    
# dibujarRectagulo(altura, ancho)

#TODO Ejercicio 2

# altura = int(input('Ingresa una altura: '))


# def dibujarTriangulo(altura):
#     for paso in range(altura):
#         print("*" * (altura - paso))

    
# dibujarTriangulo(altura)

#TODO Ejercicio 3

numero = int(input('Ingresa un numero entero: '))

def funCollatz(numero):
    while numero != 1:
        if numero % 2 == 0:
            numero = numero / 2
            print(numero)
        else:
            numero = (numero * 3) + 1
            print(numero)

funCollatz(numero)