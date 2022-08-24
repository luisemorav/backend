## Herencia

class Animal:
    def __init__(self, nro_patas, onomatopeya, color_pelaje):
        self.nro_patas = nro_patas
        self.onomatopeya = onomatopeya
        self.color_pelaje = color_pelaje

    def comoCamina(self):
        pass

    def sonido(self):
        print(f'El sonido que hace es: {self.onomatopeya}')

class Perro(Animal):
    def __init__(self, nro_patas, onomatopeya, color_pelaje, raza):
        # Instancia del constructor de la clase padre: Animal
        super().__init__(nro_patas, onomatopeya, color_pelaje)
        # super(SegundaClase).__init__(uno, dos)

        # Propiedades de la clase Perro
        self.raza = raza

    def comoCamina(self):
        print(f'Camina en {self.nro_patas} patas')

bulldog = Perro(4, "Guau", "negro", "bulldog")
bulldog.sonido()
bulldog.comoCamina()
print(bulldog.raza)

# class ClaseUno:
#     pass

# class ClaseDos(ClaseUno):
#     pass

# class ClaseTres(ClaseDos):
#     pass

# class ClaseCuatro(ClaseTres):
#     pass

# print(ClaseCuatro.__mro__)


#* Multiples Herencias
# Recursos Humanos
    # Empleado
    # Domicilio

class Empleado:
    def __init__(self, nombre, apellido, area):
        self.nombre = nombre
        self.apellido = apellido
        self.area = area

class Domicilio:
    def __init__(self, direccion, distrito, provincia, departamento):
        self.direccion = direccion
        self.distrto = distrito
        self.provincia = provincia
        self.departamento = departamento

class RecursosHumanos(Empleado, Domicilio):
    def __init__(self, nombre, apellido, area, direccion, distrito, provincia, departamento, vigente):
        Empleado.__init__(self, nombre, apellido, area)
        Domicilio.__init__(self, direccion, distrito, provincia, departamento)

        # Propidades de Recursos Humanos
        self.vigente = vigente

recursos_humanos = RecursosHumanos(
    "Carlos", "Cruz", "Desarrollo",
    "Av Mia casa 111", "Distrito Cono",
    "Lima", "Lima", True
)

print(recursos_humanos.nombre)
print(recursos_humanos.direccion)
print(recursos_humanos.vigente)