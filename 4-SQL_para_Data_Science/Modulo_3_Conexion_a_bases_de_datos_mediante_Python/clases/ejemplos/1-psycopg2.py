# Previamente si no se tiene instalado descargar: pip install psycopg2

import psycopg2

connection = psycopg2.connect(
    host='localhost', #ip
    user='postgres',
    password='catalina',
    database='postgres',
    port='5432'
)

connection.autocommit = True

def crearTabla():
    cursor = connection.cursor()
    sql = '''
            CREATE TABLE usuario(
            id serial primary key,
            nombre VARCHAR(30),
            apellido VARCHAR(30),
            email VARCHAR(30)
            ) 
          '''
    try:
        cursor.execute(sql)
    except Exception as e:
        print("No se puede crear la tabla:\n", e)
    cursor.close()

def insertarDatos(nombre,apellido,email):
    cursor = connection.cursor()
    sql = f'''
            INSERT INTO usuario (nombre,apellido,email)
                VALUES ('{nombre}','{apellido}','{email}')
          '''
    try:
        cursor.execute(sql)
    except Exception as e:
        print("No se puede insertar datos en la tabla:\n", e)
    cursor.close()

def actualizarDato(nuevo,actual):
    cursor = connection.cursor()
    sql = f''' UPDATE usuario SET nombre='{nuevo}' WHERE nombre='{actual}' '''
    try:
        cursor.execute(sql)
    except Exception as e:
        print("No se puede eliminar la tabla:\n", e)
    cursor.close()

def eliminarTabla():
    cursor = connection.cursor()
    sql = 'DROP TABLE usuario'
    try:
        cursor.execute(sql)
    except Exception as e:
        print("No se puede eliminar la tabla:\n", e)
    cursor.close()

# crearTabla()
# insertarDatos('Tomas','Lino','tomaslino@gmail.com')
# eliminarTabla()
# actualizarDato('Andres','Alfonso')