# foreach - for

# meses = ["Enero", "Febrero", "Marzo"]

# for mes in meses:
#     print(mes)

#Obtener el indice y el valor
# for index, value in enumerate(meses):
#     print(index, value)

# print(f'Fuera del scope -> {mes}')

# lista_uno = [1, 2, 3]
# lista_dos = [5, 3, 1]

# for uno in lista_uno:
#     for dos in lista_dos:
#         if uno == dos:
#             print(uno)


# for(let i=0; i<10; i++) { ... }
# range
# 1º donde empieza
# 2º hasta donde finaliza (n-1)
# 3º de cuanto en cuanto incrementa
# for numero in range(1, 10, 2):
#     print(numero)

# Ejemplo 2
persona = {
    "nombre": "Luis",
    "apellidos": "Mora",
    "cursos": ["Aritmetica", "Geometria"]
}

# for key, value in persona.items():
#     print(key, value)

# while

edad = 28

while edad > 18:
    print(f'actual -> {edad}')
    edad -= 1

    if edad == 21:
        break

