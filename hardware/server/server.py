import socket
from threading import Thread

def start_server(port, num_connections):
    sock = socket.socket()
    sock.bind(('', port))
    sock.listen(num_connections)
    return sock


def connection_thread(conn, chunk_size = 1024):
    while True:
        data = conn.recv(chunk_size)
        if data:
            print(data)
        print('asfa')


def wait_connection(sock):
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    Thread(target = connection_thread, args=(conn,)).start()