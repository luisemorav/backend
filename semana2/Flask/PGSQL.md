# PGADMIN
```
- Usuario: postgres
- Puerto: 5432
- Contraseña: (Ingresaron al instalar) admin
```

## Tipos de datos
### Numero Enteros
```
- smallint (2 bytes) -32768 a 32767
- int (4 bytes) -2147483648 a 2414783647
- bigint (8 bytes) -92233720368554775808 a 92233720368554775807
```

### Numeros Enteros Autoincrementables / Unicos
```
- smallserial <-> smallint
- serial <-> int
- bigserial <-> bigint
```

### Numeros Decimales
```
- numeric, decimal <-> 131000 digitos antes del punto, 16k digitos despues del punto
- real <-> 6 digitos decimales de precisión
- double precision <-> 15 digitos decimales de precisión
```

### Caracteres (Strings)
```
- char
ejm:
---- char(20) -> gato
---- gato(4) - en blanco (16)

- varchar (255)
- text
```

### Booleanos
```
-- boolean
- true -> 1, 'yes', 'y', 't', true
- false -> 0, 'no', 'n', 'f', false
```

### Fecha y/o Hora
### Array
### Geometria y Redes
### UUID (Identificador Unico Universal)
### JSON