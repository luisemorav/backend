# en JS -> function nombre() {  logica  }


# ? Funcion en Python
# def nombreFuncion():
#     pass

# * Función con parámetro o argumento


# def saludar(nombre):
#     print(f'Hola {nombre}, como estás')


# saludar('Luis')

# * Función con parámetros, con valor por defecto


# def saludarConNombre(nombre="Cesar", apellido="Allauca"):
#     print(f'{nombre} {apellido}')


# saludarConNombre()
# saludarConNombre('Luis', 'Mora')
# saludarConNombre(apellido="Razuri", nombre="Edgar")

# TODO Ejercicio
# Crear una funcion que reciba 2 números, donde el primer numero tinee por defecto 10, si es par imprimir la mitad de la suma, si es impar imprimir la suma

# def Ejercicio(b, a=10):
#     suma = a + b
#     if suma % 2 == 0:
#         print(suma/2)
#     else:
#         print(suma)


# a = int(input('ingresa un primer número'))
# b = int(input('Ingresa un segundo número'))

# Ejercicio(b)

# * Función con multiparámetros
# ? *args -> nombreFuncion("Valor1", "Valor2", ..., "ValorX")
# ? **kwargs -> nombreFuncion(valoruno="1", valordos="2", ..., valorx="x")

# def alumnosInscritos(*args):
#     print(args)

# # alumnosInscritos("Arturo", "Cesar", "Daniel", "Christian", "David")

# def cursosDeAlumnos(**kwargs):
#     print(kwargs)

#cursosDeAlumnos(curso_uno="Algebra", curso_dos="Artmetica", curso_tres="Matematica")

#  TODO Ejercicio 2: Crear una funcion que reciba N notas, y te indique cuantas desaprobaron y cuantas aprobaron
# nota > 10 -> Aprobado

def contarNotas(*args):
    aprobados = 0
    desaprobados = 0
    for nota in args:
        if nota > 10:
            aprobados += 1
        else:
            desaprobados += 1
    print(f'Aprobados: {aprobados}, Desaprobados: {desaprobados}')


contarNotas(12, 20, 10, 9, 7)
