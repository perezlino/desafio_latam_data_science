import psycopg2

host='localhost' 
user='postgres'
password='catalina'
database='postgres'
port='5432'

# ================================= CREAR UNA TABLA =================================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(50) NOT NULL
                )
                """)
    conn.commit()

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ======================= INSERTAR FILA A LA TABLA (FORMA 1) ========================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)",
                    ("ryan ray", "ryan@gmail.com", "ryan123")
                )
    conn.commit()

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ======================= INSERTAR FILA A LA TABLA (FORMA 2) ========================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    new_user = ("maria perez", "maria@gmail.com", "maria123")
    insert_query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"
    cur.execute(insert_query, new_user)
    conn.commit()

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ============ INSERTAR y VISUALIZAR FILA INSERTADA A LA TABLA (FORMA 1) ============
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    new_user = ("carlos zepeda", "carlos@gmail.com", "carlos123")
    insert_query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s) RETURNING *"
    cur.execute(insert_query, new_user)
    user = cur.fetchone()
    conn.commit()

    print(user)
    # (4, 'carlos zepeda', 'carlos@gmail.com', 'carlos123')

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ============ INSERTAR y VISUALIZAR FILA INSERTADA A LA TABLA (FORMA 2) ============
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    new_user = ("antonio jara", "antonio@gmail.com", "antonio123")
    insert_query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s) RETURNING(name,email)"
    cur.execute(insert_query, new_user)
    user = cur.fetchone()
    conn.commit()

    print(user)
    # ('("antonio jara",antonio@gmail.com)',)

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ================== INSERTAR MÚLTIPLES FILAS A LA TABLA (FORMA 1) ==================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    multiple_input = [
        ("luis zarate", "luis@gmail.com", "luis123"),
        ("isidora mendez", "isidora@gmail.com", "isidora123"),
        ("javiera rebolledo", "javiera@gmail.com", "javiera123")
    ]
    insert_query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"
    for input in multiple_input:
        cur.execute(insert_query, input)
    conn.commit()

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ================== INSERTAR MÚLTIPLES FILAS A LA TABLA (FORMA 2) ==================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    multiple_input = [
        ("tomas lino", "tomas@gmail.com", "tomas123"),
        ("valentina leon", "valentina@gmail.com", "valentina123"),
        ("matias rios", "matias@gmail.com", "matias123")
    ]
    insert_query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"
    cur.executemany(insert_query, multiple_input)
    conn.commit()

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 1) =================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    print(type(cur.fetchall()))

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Nos devuelve un valor de tipo <class 'list'>
'''
[(1, 'ryan ray', 'ryan@gmail.com', 'ryan123'), (2, 'maria perez', 'maria@gmail.com', 'maria123'), 
(3, 'javier peña', 'javier@gmail.com', 'javier123'), (4, 'carlos zepeda', 'carlos@gmail.com', 'carlos123'), 
(5, 'antonio jara', 'antonio@gmail.com', 'antonio123'), (6, 'luis zarate', 'luis@gmail.com', 'luis123'), 
(7, 'isidora mendez', 'isidora@gmail.com', 'isidora123'), (8, 'javiera rebolledo', 'javiera@gmail.com', 'javiera123'), 
(9, 'tomas lino', 'tomas@gmail.com', 'tomas123'), (10, 'valentina leon', 'valentina@gmail.com', 'valentina123'), 
(11, 'matias rios', 'matias@gmail.com', 'matias123')]
'''
# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 2) =================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Nos devuelve valores de tipo <class 'tuple'>
'''
(1, 'ryan ray', 'ryan@gmail.com', 'ryan123')
(2, 'maria perez', 'maria@gmail.com', 'maria123')
(3, 'javier peña', 'javier@gmail.com', 'javier123')
(4, 'carlos zepeda', 'carlos@gmail.com', 'carlos123')        
(5, 'antonio jara', 'antonio@gmail.com', 'antonio123')       
(6, 'luis zarate', 'luis@gmail.com', 'luis123')
(7, 'isidora mendez', 'isidora@gmail.com', 'isidora123')     
(8, 'javiera rebolledo', 'javiera@gmail.com', 'javiera123')  
(9, 'tomas lino', 'tomas@gmail.com', 'tomas123')
(10, 'valentina leon', 'valentina@gmail.com', 'valentina123')
(11, 'matias rios', 'matias@gmail.com', 'matias123')
'''
# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 3) =================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row[0], row[1])

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Nos devuelve valores de tipo <class 'int'> y <class 'str'>
'''
1 ryan ray
2 maria perez      
3 javier peña      
4 carlos zepeda    
5 antonio jara     
6 luis zarate      
7 isidora mendez   
8 javiera rebolledo
9 tomas lino       
11 matias rios
'''
# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 4) =================
from psycopg2 import extras

cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.DictCursor)

    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(type(row))

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Nos devuelve valores de tipo <class 'psycopg2.extras.DictRow'>
# Parecen listas pero los podemos trajar como diccionarios
'''
[1, 'ryan ray', 'ryan@gmail.com', 'ryan123']
[2, 'maria perez', 'maria@gmail.com', 'maria123']
[3, 'javier peña', 'javier@gmail.com', 'javier123']
[4, 'carlos zepeda', 'carlos@gmail.com', 'carlos123']        
[5, 'antonio jara', 'antonio@gmail.com', 'antonio123']       
[6, 'luis zarate', 'luis@gmail.com', 'luis123']
[7, 'isidora mendez', 'isidora@gmail.com', 'isidora123']     
[8, 'javiera rebolledo', 'javiera@gmail.com', 'javiera123']  
[9, 'tomas lino', 'tomas@gmail.com', 'tomas123']
[10, 'valentina leon', 'valentina@gmail.com', 'valentina123']
[11, 'matias rios', 'matias@gmail.com', 'matias123']
'''
# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 5) =================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.DictCursor)

    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row['name'], row['email'])

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Parecen listas pero los podemos trabajar como diccionarios
'''
ryan ray ryan@gmail.com
maria perez maria@gmail.com 
javier peña javier@gmail.com
carlos zepeda carlos@gmail.com
antonio jara antonio@gmail.com
luis zarate luis@gmail.com
isidora mendez isidora@gmail.com
javiera rebolledo javiera@gmail.com
tomas lino tomas@gmail.com
valentina leon valentina@gmail.com
matias rios matias@gmail.com
'''
# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 6) =================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Parecen listas pero los podemos trabajar como diccionarios
'''
RealDictRow([('id', 1), ('name', 'ryan ray'), ('email', 'ryan@gmail.com'), ('password', 'ryan123')])
RealDictRow([('id', 2), ('name', 'maria perez'), ('email', 'maria@gmail.com'), ('password', 'maria123')])
RealDictRow([('id', 3), ('name', 'javier peña'), ('email', 'javier@gmail.com'), ('password', 'javier123')])
RealDictRow([('id', 4), ('name', 'carlos zepeda'), ('email', 'carlos@gmail.com'), ('password', 'carlos123')])        
RealDictRow([('id', 5), ('name', 'antonio jara'), ('email', 'antonio@gmail.com'), ('password', 'antonio123')])       
RealDictRow([('id', 6), ('name', 'luis zarate'), ('email', 'luis@gmail.com'), ('password', 'luis123')])
RealDictRow([('id', 7), ('name', 'isidora mendez'), ('email', 'isidora@gmail.com'), ('password', 'isidora123')])     
RealDictRow([('id', 8), ('name', 'javiera rebolledo'), ('email', 'javiera@gmail.com'), ('password', 'javiera123')])  
RealDictRow([('id', 9), ('name', 'tomas lino'), ('email', 'tomas@gmail.com'), ('password', 'tomas123')])
RealDictRow([('id', 10), ('name', 'valentina leon'), ('email', 'valentina@gmail.com'), ('password', 'valentina123')])
RealDictRow([('id', 11), ('name', 'matias rios'), ('email', 'matias@gmail.com'), ('password', 'matias123')])
'''
# ================== VISUALIZAR LOS REGISTROS DE LA TABLA (FORMA 7) =================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row['name'], row['email'])

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# Parecen listas pero los podemos trabajar como diccionarios
'''
ryan ray ryan@gmail.com
maria perez maria@gmail.com        
javier peña javier@gmail.com       
carlos zepeda carlos@gmail.com     
antonio jara antonio@gmail.com     
luis zarate luis@gmail.com
isidora mendez isidora@gmail.com   
javiera rebolledo javiera@gmail.com
tomas lino tomas@gmail.com
valentina leon valentina@gmail.com 
matias rios matias@gmail.com    
'''
# =================== ELIMINAR REGISTRO DE LA TABLA Y VISUALIZARLO ==================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    delete_input = 11
    delete_user = "DELETE FROM users WHERE id = '{}' RETURNING *".format(delete_input)
    cur.execute(delete_user, delete_input)

    user_deleted = cur.fetchone()
    print(user_deleted)
    conn.commit()

    cur.execute('SELECT * FROM users')
    for user in cur.fetchall():
        print(user)

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
'''
RealDictRow([('id', 11), ('name', 'matias rios'), ('email', 'matias@gmail.com'), ('password', 'matias123')]) ==> VALOR ELIMINADO
RealDictRow([('id', 1), ('name', 'ryan ray'), ('email', 'ryan@gmail.com'), ('password', 'ryan123')])
RealDictRow([('id', 2), ('name', 'maria perez'), ('email', 'maria@gmail.com'), ('password', 'maria123')])
RealDictRow([('id', 3), ('name', 'javier peña'), ('email', 'javier@gmail.com'), ('password', 'javier123')])
RealDictRow([('id', 4), ('name', 'carlos zepeda'), ('email', 'carlos@gmail.com'), ('password', 'carlos123')])        
RealDictRow([('id', 5), ('name', 'antonio jara'), ('email', 'antonio@gmail.com'), ('password', 'antonio123')])       
RealDictRow([('id', 6), ('name', 'luis zarate'), ('email', 'luis@gmail.com'), ('password', 'luis123')])
RealDictRow([('id', 7), ('name', 'isidora mendez'), ('email', 'isidora@gmail.com'), ('password', 'isidora123')])     
RealDictRow([('id', 8), ('name', 'javiera rebolledo'), ('email', 'javiera@gmail.com'), ('password', 'javiera123')])  
RealDictRow([('id', 9), ('name', 'tomas lino'), ('email', 'tomas@gmail.com'), ('password', 'tomas123')])
RealDictRow([('id', 10), ('name', 'valentina leon'), ('email', 'valentina@gmail.com'), ('password', 'valentina123')])
'''
# ========================= SELECCIONAR REGISTROS DE LA TABLA =======================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    select_input = 1
    select_user = "DELETE FROM users WHERE id = '{}' RETURNING *".format(select_input)
    cur.execute(select_user, select_input)

    user_selected = cur.fetchone()
    print(user_selected)

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
'''
RealDictRow([('id', 1), ('name', 'ryan ray'), ('email', 'ryan@gmail.com'), ('password', 'ryan123')])
'''
# ==================== ACTUALIZAR REGISTROS DE LA TABLA (FORMA 1) ===================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    update_input = ('alfredo soto','alfredo@gmail.com','1')
    update_user = "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING *"
    cur.execute(update_user,update_input)

    conn.commit()

    new_user = cur.fetchone()
    print(new_user)

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

'''
RealDictRow([('id', 1), ('name', 'alfredo soto'), ('email', 'alfredo@gmail.com'), ('password', 'ryan123')])
'''
# ================================= BORRAR LA TABLA =================================
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('DROP TABLE IF EXISTS users')
    conn.commit()

except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()