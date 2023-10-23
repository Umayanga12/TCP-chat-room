import socket
import threading

nickname = input("Enter the Nickname : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# need to add the localhost and the port number of the host or the server
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)
        except:
            print("Error occurred !!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}:{input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
