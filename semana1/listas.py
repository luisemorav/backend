# Mutable: Nos ayuda a almacenar mas de un valor

#! Forma incorrecta
# persona_uno = "Carlos"
# persona_dos = "Luis"
# persona_tres = "Cesar"

#? Forma correcta
personas = ["Carlos", "Luis", "Cesar"]

# n - 1

print(personas)
print(personas[2])


# Funciones

#append -> agregar un valor al final de una lista
personas.append("Alan")
print(f'append -> {personas}')

# insert -> agrega un valor en una lista segun la posicion o indice mencionado
personas.insert(0, "David")
print(f'insert -> {personas}')

# index -> retorna el indice del valor mencionado
indice_luis = personas.index("Luis")
print(f'index -> {indice_luis}')

# extend -> unir dos listas
personas_nuevas = ["Andres", "Daniel", "Arturo"]
personas.extend(personas_nuevas)
print(f'extend -> {personas}')

# remove -> elimina un valor de una lista
personas.remove("Alan")
print(f'remove -> {personas}')

# pop -> elimina un valor segun la posición o el indice
personas.pop(3) # ultimo valor -> -1
print(f'pop -> {personas}')

#sort -> ordena los valores de una lista, por defecto de menor a mayor
# reverse=False -> menor a mayor
# reverse=True -> mayor a menor
personas.sort(reverse=True) 
print(f'sort -> {personas}')

# count -> retorna las veces que existe un elemento
personas.append("Daniel")
daniel_contador = personas.count("Daniel")
print(f'count -> {daniel_contador}')

# len -> cuenta los elementos de una estructura de dato | length
print(f'Total de personas: {len(personas)}')