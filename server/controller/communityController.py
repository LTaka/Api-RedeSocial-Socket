from model import communityModel

def create_community(nome):
    community = communityModel.create_community(nome)

    if(community != False):
        response = {
            'status': 'SUCCESS', 
            'id_community': community
        }
    else:
        response = {
            'status': 'ERROR'
        }
    return response
    
def create_user_community(id_user, id_community):
    user_community = communityModel.create_user_community(id_user, id_community)

    if(user_community != False):
        response = {
            'status': 'SUCCESS'
        }
    else:
        response = {
            'status': 'ERROR'
        }
    return response

def get_community_by_Name(name):
    community,id = communityModel.get_community_by_Name(name)

    response = {
        'communities':community,
        'id_community':id
    }

    return response

def get_community_by_ID(id_community):
    community = communityModel.get_community_by_ID(id_community)

    response = {
        'name':community[0][0]
    }

    return response

def get_all_community_by_id_user(id_universitario):
    communities_ids = communityModel.get_all_community_by_id_user(id_universitario)

    response = []
    for id_community in communities_ids:
        community_name = communityModel.get_community_by_ID(id_community[0])
        response.append({
            'id_community':id_community[0],
            'name':community_name[0][0]
        })

    return response

def get_all_community():
    communities = communityModel.get_all_community()

    response = []
    for community in communities:
        response.append({
            'id_community':community[0],
            'name':community[1]
        })

    return response