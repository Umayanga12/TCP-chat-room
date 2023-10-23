import threading
import socket

# server address or localhost
host = '127.0.0.1'
port = 55555

# creating the sever
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

# server is in listing mode
server.listen()

clients = []
nicknames = []


def broadcasr(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcasr(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcasr(f"{nickname} is left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break


def recieve():
    while True:
        client, address = server.accept()
        print(f'connected with the  {address}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'client nickname is {nickname}')
        broadcasr(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listing.....")
recieve()
