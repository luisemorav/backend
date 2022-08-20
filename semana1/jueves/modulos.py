# import camelcase
from camelcase import CamelCase as ClaseCamel

instancia = ClaseCamel()
texto = "hola chicos"
print(instancia.hump(texto))
