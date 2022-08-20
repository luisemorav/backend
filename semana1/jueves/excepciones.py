try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print('El valor ingresado no es un número')
except ZeroDivisionError:
    print('El valor ingresado debe ser mayor a 0')
except KeyboardInterrupt:
    print('\nLa aplicación se cerró\n')
except Exception as err:
    print(err.__class__)
    print('Hay un error')
else: #! Se va ejecutar siempre y cuando no haya un error
    print(f'No hubo un error -> {resultado}')
finally: #? Se va ejectuar al final, aunque este bien o haya un error
    print('Siempre')
