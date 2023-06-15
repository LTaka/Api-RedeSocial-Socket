import asyncio
import threading
import json
from connect import Connect

class Server():
    def __init__(self):
        # connecta o servido ao socket
        self.socket = Connect()
        print(f'Servidor escutando em {self.socket.host}:{self.socket.port}')
        asyncio.run(self.handle_connections())

    async def handle_connections(self):
        loop = asyncio.get_running_loop()
        while True:
            self.client_socket, self.addr = await loop.run_in_executor(None, self.socket.server_socket.accept)
            print(f'Cliente conectado: {self.addr[0]}:{self.addr[1]}')
            # Inicia uma thread para processar as requisições do cliente
            threading.Thread(target=self.handle_client, args=(self.socket.port,)).start()
  

    def handle_client(self, port):
        # Processa as mensagens recebidas do cliente
        while True:
            data = self.client_socket.recv(port)  # Recebe dados do cliente
            if not data:
                break
            # Processa os dados recebidos
            data = data.decode()
            # Analise os dados JSON recebidos
            json_data = json.loads(data)
            # Processar a requisição
            response = self.process_request(json_data)
            self.client_socket.send(json.dumps(response).encode())  # Envia os dados processados de volta para o cliente
        self.client_socket.close()

    # funcao para processar a requisicao
    def process_request(self, request):
        # verifica o tipo da requisicao
        if request['method'] == 'GET':
            # processar requisicao GET
            response = self.socket.get(request)
        elif request['method'] == 'POST':
            # processar requisicao POST
            response = self.socket.post(request)
        else:
            response = {'message': 'Metodo nao suportado'}
        
        return response    

if __name__ == '__main__':
    Server()