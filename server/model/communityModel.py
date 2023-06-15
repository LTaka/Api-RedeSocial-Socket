from dataBase import dataBase

def create_community(name):
    conn = dataBase.DB().db
    cursor = conn.cursor()

    cursor.execute("INSERT INTO community (name) VALUES (?)", (name, ))

    last_id = cursor.lastrowid

    if (last_id == None):
        return False
    # Confirmar as alterações feitas no banco de dados
    conn.commit()
    conn.close()

    return last_id

def create_user_community(id_user, id_community):
    conn = dataBase.DB().db
    cursor = conn.cursor()

    cursor.execute("INSERT INTO communities_has_users (id_user, id_community) VALUES (?, ?)", (id_user, id_community, ))

    last_id = cursor.lastrowid

    if (last_id == None):
        return False
    # Confirmar as alterações feitas no banco de dados
    conn.commit()
    conn.close()

    return last_id

def get_community_by_ID(id_community):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    comunidade = cursor.execute("""
        SELECT name FROM community WHERE id_community = ?;
    """, (id_community,)).fetchall()

    conn.close()

    return comunidade

def get_community_by_Name(name):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    comunidades=[]
    id=[]
    comunidade = cursor.execute("""
        SELECT * FROM community WHERE name LIKE ?;
    """, ( name + '%',)).fetchall()

    conn.close()

    for comunity in comunidade:
        comunidades.append(comunity[1])
        id.append(comunity[0])

    return comunidades,id

def get_all_community_by_id_user(id_user):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    comunidades = cursor.execute("""
        SELECT id_community FROM communities_has_users WHERE id_user = ?;
    """, (id_user,)).fetchall()

    conn.close()

    return comunidades

def get_all_community():
    conn = dataBase.DB().db
    cursor = conn.cursor()
    comunidades = cursor.execute("""
        SELECT * FROM community;
    """).fetchall()

    conn.close()

    return comunidades