from dataBase import dataBase

def create_user(name, email, password, course, university):
    conn = dataBase.DB().db
    cursor = conn.cursor()

    cursor.execute("INSERT INTO user (name, email, password, course, university) VALUES (?, ?, ?, ?, ?)", (name, email, password, course, university))

    last_id = cursor.lastrowid

    if (last_id == None):
        return False
    # Confirmar as alterações feitas no banco de dados
    conn.commit()
    conn.close()

    return True

def get_all_users():
    conn = dataBase.DB().db
    cursor = conn.cursor()
    usuarios = []
    tuplaUsuarios = cursor.execute("""
        SELECT * FROM user;
    """).fetchall()

    conn.close()

    for usuario in tuplaUsuarios:
        usuarios.append(usuario[1])

    return usuarios

def get_user_by_ID(id_user):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    usuario = cursor.execute("""
        SELECT * FROM user WHERE id_user = ?;
    """, (id_user,)).fetchall()

    conn.close()

    return usuario

def get_user_by_Name(name):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    usuarios = []
    id = []
    usuario = cursor.execute("""
        SELECT * FROM user WHERE name LIKE ?;
    """, (name + '%',)).fetchall()

    conn.close()
    for user in usuario:
        usuarios.append(user[1])
        id.append(user[0])

    return id,usuarios

def get_user_by_email(email):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    usuario = cursor.execute("""
        SELECT * FROM user WHERE email = ?;
    """, (email,)).fetchall()

    conn.close()

    return usuario