import socket

SERVER_ADDRESS = ('localhost', 10125)  # Endereço do servidor
client_code = None

# Cria o socket do cliente
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Solicita ao usuário o código do cliente
while not client_code:
    client_code = input('Digite o código do cliente: ')

# Envia mensagens para o servidor
while True:
    try:
        # Solicita ao usuário a mensagem
        message = input('Digite a mensagem: ')

        # Envia a mensagem para o servidor
        message = f'({client_code}) : {message}'.encode()
        sock.sendto(message, SERVER_ADDRESS)

        # Recebe a resposta do servidor
        response, _ = sock.recvfrom(1024)
        print(f'Mensagem enviada para o servidor: {message.decode()}')
        print(f'Resposta recebida do servidor: {response.decode()}')
    except socket.error as error:
        print('Servidor não disponível no momento')
