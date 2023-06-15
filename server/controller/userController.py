import json
from model import userModel

def create_user(nome, email, senha, curso, universidade):
    user = userModel.create_user(nome, email, senha, curso, universidade)

    if(user):
        response = {
            'status': 'SUCCESS'
        }
    else:
        response = {
            'status': 'ERROR'
        }
    return response

def get_user_by_ID(id_univesitario):
    user = userModel.get_user_by_ID(id_univesitario)

    response = {
        'id_user':user[0][0],
        'name':user[0][1],
        'email':user[0][2],
        'password':user[0][3],
        'course':user[0][4],
        'university':user[0][5]
    }

    return response

def get_user_by_Name(name):
    id,user = userModel.get_user_by_Name(name)

    response = {
        'user':user,
        'id_user':id
    }

    return response
    
def get_user_by_email(email,senhaRecebida):
    user = userModel.get_user_by_email(email)

    response = {
            'status':'ERROR'
        }
    
    if (user):
        #verifica a senha do baco e a receida
        senhaBD=user[0][3] 
        if(senhaBD==senhaRecebida):
            response = {
                'status':'SUCCESS',
                'id_user':user[0][0]
            }
    return response