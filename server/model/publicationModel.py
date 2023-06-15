from dataBase import dataBase

def create_publication(id_user, id_community, description):
    conn = dataBase.DB().db
    cursor = conn.cursor()

    cursor.execute("INSERT INTO publication (id_user, id_community, description, likes_amount) VALUES (?, ?, ?, ?)", (id_user, id_community, description, 0))

    last_id = cursor.lastrowid

    if (last_id == None):
        return False
    # Confirmar as alterações feitas no banco de dados
    conn.commit()
    conn.close()

    return True

def get_all_publication_by_id_community(id_community):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    publicacoes = cursor.execute("""
        SELECT * FROM publication WHERE id_community = ?;
    """, (id_community,)).fetchall()

    conn.close()

    return publicacoes

def get_publication_by_ID(id_publication):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    publicacao = cursor.execute("""
        SELECT * FROM publication WHERE id_publication = ?;
    """, (id_publication,)).fetchall()

    conn.close()

    return publicacao

def like_publication(id_publication, id_user):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    user = cursor.execute("""
        SELECT id_user from publications_has_like WHERE id_user = ? AND id_publication = ?
    """, (id_user, id_publication, )).fetchone()

    increment = 1

    # verifica se usuario ja deu like
    if (user):
        # usuario ja deu like, ação: deslike
        cursor.execute("""
        UPDATE publication SET likes_amount = likes_amount - ? WHERE id_publication = ?
        """, (increment, id_publication, ))
        cursor.execute("""
            DELETE FROM publications_has_like WHERE id_user = ? AND id_publication = ?
        """, (id_user, id_publication, ))
    else:
        # usuario não deu like, ação: like
        cursor.execute("""
        UPDATE publication SET likes_amount = likes_amount + ? WHERE id_publication = ?
        """, (increment, id_publication, ))
        cursor.execute("""
            INSERT INTO publications_has_like (id_user, id_publication) VALUES (?, ?)
        """, (id_user, id_publication, ))

    conn.commit()
    conn.close()