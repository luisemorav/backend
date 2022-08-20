# Ejercicio 1
# Solicitar una palabra y validarla si esta es un palindromo
# palabra = input("Ingresa una palabra: ")

# palabra_inversa = palabra[::-1]

# if palabra == palabra_inversa:
#     print('La palabra es palindromo')
# else:
#     print('La palabra no es un palindromo')

# Ejercicio 2
# Solicitar el año en que nacimos, este mismo se va a iterar restando el año actual, de tal manera nos mostraria cuanto saños tenemos en cada año iterado
year = int(input("Ingresa tu año de nacimiento: "))
edad = 0

while year < 2021:
    year += 1
    edad += 1
    print(f'En el año {year}, tenía {edad} años.')
    if year == 2021:
        print(f'En el año {year + 1}, tengo {edad + 1} años.')
        break