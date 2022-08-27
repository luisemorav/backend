from psycopg2 import connect

connection = connect(
    user='postgres',
    password='admin', #La contraseña que se colocó en postgres
    host='localhost',
    port=5432,
    database='tecsup'
)

cursor = connection.cursor()

# cursor.execute("SELECT * FROM area")
# cursor.execute("SELECT * FROM area WHERE id=2")
#cursor.execute("SELECT * FROM area WHERE id IN (1, 2)")

#? fetchone -> Usar cuando la consulta traiga una fila
#? fetchall -> Usar cuando la consulta traiga mas de una fila

# record = cursor.fetchone()
#record = cursor.fetchall()
#print(record)


#TODO Transaccionalidad Insert, Update, Delete

try:
    cursor.execute("INSERT INTO area(name) VALUES ('Química');")
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f'Ocurrio un error -> {e}')

#! Obligatorio cerrar la sesión y la conexión despues de la consulta
cursor.close()
connection.close()