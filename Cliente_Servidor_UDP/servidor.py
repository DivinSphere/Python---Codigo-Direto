import socket
import time

# Constantes
HOST = ''
PORT = 10125
MAX_CLIENTS = 10
BUFFER_SIZE = 1024

# Cria o socket do servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        sock.bind((HOST, PORT))
        break
    except OSError:
        print(f'A porta {PORT} já está em uso. Tentando novamente em 1 segundo...')
        time.sleep(1)
        continue

print(f'Servidor escutando na porta {PORT}...')

clients = {}

def register_new_client(address):
    """
    Registra um novo cliente e retorna o código do cliente.
    """
    code = len(clients) + 1
    clients[address] = code
    print(f'Novo cliente conectado: {address} (Código: {code})')
    return code

def handle_client_message(message, address):
    """
    Manipula a mensagem recebida de um cliente e retorna a resposta do servidor.
    """
    sender_code = clients[address]
    print(f'(Código: {sender_code}) Mensagem recebida do cliente {address}: {message}')
    return f'Resposta do servidor para o cliente {sender_code}'.encode()

def run_server():
    """
    Executa o servidor.
    """
    try:
        while True:
            # Recebe a mensagem do cliente
            data, address = sock.recvfrom(BUFFER_SIZE)

            # Verifica se o cliente já está registrado
            if address not in clients and len(clients) < MAX_CLIENTS:
                register_new_client(address)

            if address in clients:
                # Manipula a mensagem do cliente e envia a resposta de volta
                message = data.decode()
                response = handle_client_message(message, address)
                sock.sendto(response, address)
    except KeyboardInterrupt:
        print('\nEncerrando o servidor...')
    finally:
        sock.close()

# Executa o servidor
if __name__ == '__main__':
    run_server()
