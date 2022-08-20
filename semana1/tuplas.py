# Inmutable
personas = ("Alan", "Andres", "Cesar", "David")

# index -> retorna el indice de un valor mencionado
indice_cesar = personas.index("Cesar")
print(f'index -> {indice_cesar}')

# count -> retorna las veces que existe un elemento
david_contador = personas.count("David")
print(f'David Count -> {david_contador}')

##############################################
# list -> convertir o crear una lista

# tuple -> convertir o crear una tupla
personas_lista = list(personas)
personas_lista.append("Eder")
print(type(personas_lista))
print(f'append -> {personas_lista}')

personas = tuple(personas_lista)
print(type(personas))
print(f'nueva tupla -> {personas}')