import psycopg2

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Client(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(60) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        phone INTEGER NULL);    
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Client_Phone(
        id SERIAL PRIMARY KEY,
        id_client INTEGER NOT NULL REFERENCES Client(id),
        phone INTEGER);
    """)
    conn.commit()

def add_client(first_name, last_name, email, phone=None):
    cur.execute("""
    INSERT INTO Client(first_name, last_name, email, phone)
        VALUES(%s, %s, %s, %s) RETURNING id;
    """, (first_name, last_name, email, phone))

    id_ = cur.fetchone()
    if phone != None:
        cur.execute("""
        INSERT INTO Client_Phone(id_client, phone)
            VALUES(%s, %s);
        """, (id_, phone))
        conn.commit()

def add_phone(id_client, phone):
    cur.execute("""
    INSERT INTO Client_Phone(id_client, phone)
        VALUES(%s, %s);
    """, (id_client, phone))

    cur.execute("""
    UPDATE Client
    SET phone=%s
    WHERE id=%s;
    """, (phone, id_client))
    conn.commit()


def change_client(id, first_name=None, last_name=None, email=None, phone=None):
    if first_name != None:
        cur.execute("""
        UPDATE Client
        SET first_name=%s
        WHERE id=%s;
        """, (first_name, id))

    if last_name != None:
        cur.execute("""
        UPDATE Client
        SET last_name=%s
        WHERE id=%s;
        """, (last_name, id))

    if email != None:
        cur.execute("""
        UPDATE Client
        SET email=%s
        WHERE id=%s;
        """, (email, id))

    if phone != None:
        cur.execute("""
        UPDATE Client
        SET phone=%s
        WHERE id=%s;
        """, (phone, id))

        cur.execute("""
        INSERT INTO Client_Phone(id_client, phone)
        VALUES(%s, %s);
        """, (id, phone))
    conn.commit()


def del_phone(client_id, phone):
    cur.execute("""
    DELETE FROM Client_Phone
    WHERE id_client=%s AND phone=%s;
    """, (client_id, phone))

    cur.execute("""
    SELECT phone FROM Client
        WHERE id=%s;
    """, (client_id,))
    x = cur.fetchall()[0][0]

    if int(x) == phone:
        cur.execute("""
        UPDATE Client
        SET phone = NULL
        WHERE id=%s;
        """, (client_id,))
    conn.commit()
def search(first_name=None, last_name=None, email=None, phone=None):
    if phone != None:
        cur.execute("""
        SELECT id_client FROM Client_Phone
        WHERE phone=%s;
        """, (phone,))
        id_ = cur.fetchone()

        cur.execute("""
        SELECT * FROM Client
        WHERE id=%s;
        """, (id_,))
        return print(cur.fetchone())

    else:
        cur.execute("""
        SELECT * FROM client c
        WHERE first_name=%s OR last_name=%s OR email=%s;
        """, (first_name, last_name, email))
        return print(cur.fetchone())


with psycopg2.connect(database="client_bd", user="postgres", password=input('Введите пароль postgres: ')) as conn:
    with conn.cursor() as cur:
        pass
