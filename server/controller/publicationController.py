from model import publicationModel

def create_publication(id_user, id_community, description):
    publication = publicationModel.create_publication(id_user, id_community, description)

    if(publication):
        response = {
            'status': 'SUCCESS'
        }
    else:
        response = {
            'status': 'ERROR'
        }
    return response

def get_all_publication_by_id_community(id_comunidade):
    publications = publicationModel.get_all_publication_by_id_community(id_comunidade)

    response = []
    for publication in publications:
        response.append({'id_publication':publication[0],
                         'description':publication[3],
                         'likes_amount':publication[4]})
    return response

def get_publication_by_ID(id_publicacao):
    publicacao = publicationModel.get_publication_by_ID(id_publicacao)

    response = {
        'id_publication':publicacao[0][0],
        'id_user':publicacao[0][1],
        'id_community':publicacao[0][2],
        'description':publicacao[0][3],
        'likes_amount':publicacao[0][4]
    }

    return response

def like_publication(id_publication, id_user):
    publicationModel.like_publication(id_publication, id_user)
