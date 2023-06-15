from dataBase import dataBase

def create_comment(id_user, id_publication, description):
    conn = dataBase.DB().db
    cursor = conn.cursor()

    cursor.execute("INSERT INTO comment (id_user, id_publication, description) VALUES (?, ?, ?)", (id_user, id_publication, description))

    last_id = cursor.lastrowid

    if (last_id == None):
        return False
    # Confirmar as alterações feitas no banco de dados
    conn.commit()
    conn.close()

    return True

def get_all_comments_by_id_publication(id_publication):
    conn = dataBase.DB().db
    cursor = conn.cursor()
    comentarios = cursor.execute("""
        SELECT * FROM comment WHERE id_publication = ?;
    """, (id_publication,)).fetchall()

    conn.close()

    return comentarios