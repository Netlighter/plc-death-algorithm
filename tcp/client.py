import socket
import threading

def receive(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(e)
            client.close()
            break

def write(client, message):
    client.send(message.encode('utf-8'))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 7777))
    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()
    return client
