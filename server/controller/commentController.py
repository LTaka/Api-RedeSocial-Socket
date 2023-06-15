from model import commentModel

def create_comment(id_user, id_publication, description):
    comment = commentModel.create_comment(id_user, id_publication, description)

    if(comment):
        response = {
            'status': 'SUCCESS'
        }
    else:
        response = {
            'status': 'ERROR'
        }
    return response

def get_all_comments_by_id_publication(id_publicacao):
    comments = commentModel.get_all_comments_by_id_publication(id_publicacao)

    response = []
    for comment in comments:
        response.append({'id_comment':comment[0],
                         'description':comment[3]})
    return response