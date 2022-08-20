# Variables de texto

nombre = "Luis"
apellido = "Mora"
texto = """
Buenos dias:
    La carta redactada...
    ...
"""

texto_en_linea = (
    "Hola, como estas? "
    "es tarde por alla? "
    "buenas noches"
)

# Operadores de salida -> print

print(nombre)
print(texto)
print(texto_en_linea)

# Variables numericos
numero_entero = 10
numero_decimal = 10.50

## Concatenación
print(nombre + apellido)
print(nombre, apellido)
# f-string
print(f"{nombre} {apellido}")

# Dinamismo
# type -> nos va retornar el tipo de variable
print(type(nombre))
print(type(numero_entero))
print(type(numero_decimal))

# Booleanas
verdadero = True
falso = False

# Variable ocn valor nulo
variable_nulo = None

# Asignacion múltiple
persona, nacionalidad = "Juan", "Peruano"
print(persona)
print(nacionalidad)
print(persona, nacionalidad)