import socket, json
from controller import userController, communityController, publicationController, commentController

class Connect():
    def __init__(self):
        self.host = '127.0.0.1'  # Endereço IP do servidor
        self.port = 42020 # Porta utilizada pelo servidor
        # Cria um objeto socket TCP/IP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket do servidor
        self.server_socket.bind((self.host, self.port))  # Associa o socket ao endereço e porta
        self.server_socket.listen(5)  # Aguarda conexões

    def get(self, request):
        # user requests
        if (request['entity'] == 'user'):
            if(request['type'] == 'byID'):
                # user by id
                return userController.get_user_by_ID(request['value'])
            elif(request['type'] == 'byName'):
                # user by name  
                return userController.get_user_by_Name(request['value'])
        # community requests
        elif(request['entity'] == 'community'):
            if (request['type'] == 'byName'):
                # community by name
                return communityController.get_community_by_Name(request['value'])
            elif (request['type'] == 'byID'):
                return communityController.get_community_by_ID(request['value'])
            elif (request['type'] == 'all'):
                if(request['value'] != None):
                    #  all community by id_user
                    return communityController.get_all_community_by_id_user(request['value'])
                else:
                    # all community
                    return communityController.get_all_community()
            
        # publication requests
        elif(request['entity'] == 'publication'):
            if (request['type'] == 'byID'):
                # publication by ID
                return publicationController.get_publication_by_ID(request['value'])
            elif (request['type'] == 'all'):
                # all publication by id_comunidade
                return publicationController.get_all_publication_by_id_community(request['value'])
        # comment requests
        elif(request['entity'] == 'comment'):
            if ((request['type'] == 'all')):
                # all comment by id_publication
                return commentController.get_all_comments_by_id_publication(request['value'])
            
    def post(self, request):
        # login
        if(request['usage'] == 'login'):
            return userController.get_user_by_email(request['email'],request['password'])
        # user register
        elif(request['usage'] == 'user_register'):
            return userController.create_user(request['name'],
                                            request['email'],
                                            request['password'],
                                            request['course'],
                                            request['university'])
        # community register
        elif(request['usage'] == 'community_register'):
            return communityController.create_community(request['name'])
        # user register in community
        elif(request['usage'] == 'user_register_community'):
            return communityController.create_user_community(request['id_user'],
                                                            request['id_community'])
        # publication register
        elif(request['usage'] == 'publication_register'):
            return publicationController.create_publication(request['id_user'],
                                                            request['id_community'],
                                                            request['description'])
        # comment register
        elif(request['usage'] == 'comment_register'):
            return commentController.create_comment(request['id_user'],
                                                    request['id_publication'],
                                                    request['description'])
        # publication like
        elif(request['usage'] == 'like'):
            return publicationController.like_publication(request['id_publication'],
                                                        request['id_user'])