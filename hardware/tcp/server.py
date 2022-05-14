import socket
from threading import Thread

CONNECTIONS = []

def start_server(port, num_connections):
    sock = socket.socket()
    sock.setblocking(1)
    sock.bind(('', port))
    sock.listen(num_connections)
    CONNECTIONS = []
    return sock


def connection_thread(conn, chunk_size = 1024):
    while True:
        try:
            data = conn.recv(chunk_size).decode()
            if data:
                print(data)
        except: 
            conn.close()


def wait_connection(sock):
    while True: 
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        CONNECTIONS.append 
        Thread(target = connection_thread, args=(conn,)).start()