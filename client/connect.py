import socket
import json

class Connect():
    def __init__(self):
        self.host = '127.0.0.1'  # Endereço IP do servidor
        self.port = 42020  # Porta utilizada pelo servidor
        self.socket_connect()

    def socket_connect(self):    
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket do cliente
        self.client_socket.connect((self.host, self.port))  # Conecta ao servidor

    def request(self,req):
        buffer_size = 4096 
        self.client_socket.send(json.dumps(req).encode())  # Envia a mensagem para o servidor
        # Recebe a resposta do servidor
        response = self.client_socket.recv(buffer_size )
        return response
    
    def finishConnection(self):
        self.client_socket.close()

    def typeConnect(self,req):
        response = json.loads( self.request(req))
        self.finishConnection()
        return response