from threading import Thread
from datetime import datetime
import socket
import psycopg2
import os
from dotenv import load_dotenv

from urllib.parse import urlparse
CONNECTIONS = []
load_dotenv()
conn_config_file = None
db = None


def start_server(port, num_connections):
    sock = socket.socket()
    sock.setblocking(1)
    sock.bind(('', port))
    sock.listen(num_connections)
    CONNECTIONS = []
    return sock

def connect_db():
    global db
    uri = os.getenv("DB_URL")
    print(f"Trying to establish connection to database ob address {uri}")
    result = urlparse(uri)
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port
    connection = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname,
        port = port
    )
    print(f"Connected to database {database}!")
    db = connection

def add_sensor_value(sensor, value):
    with db.cursor() as cursor:
        print(f"[DATABASE] Inserting '{sensor}' value of {value}")
        cursor.execute(f"SELECT sensor_id FROM \"SENSOR\" WHERE sensor_name = '{sensor}'")
        sensor_id = cursor.fetchone()[0]
        print(f"INSERT INTO \"SENSOR_VALUE\" VALUES ({sensor_id}, now(), {value});")
        cursor.execute(f"INSERT INTO \"SENSOR_VALUE\" VALUES ({sensor_id}, now(), {value})")
        db.commit()

def process_message(conn, msg: str):
    if msg.startswith("[SEND SQL]"):
        msg = msg[11:]
        process_sql_query(msg)
    elif msg.startswith("[]")
        

def process_sql_query(msg):
    if msg.startswith("[SENSOR]"):
        msg = msg[9:].split(":")
        add_sensor_value(msg[0], msg[1])

def connection_thread(conn, chunk_size = 1024):
    while True:
        try:
            data = conn.recv(chunk_size).decode()
            if data:
                process_message(conn, data)
        except Exception as e:
            print(f"Connection {conn} closed.")
            print(f"[EXCEPTION] {e}")
            conn.close()
            break


def wait_connection(sock):
    while True: 
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        CONNECTIONS.append(conn)
        Thread(target = connection_thread, args=(conn,)).start()

if __name__ == "__main__":
    socket = start_server(7777, 3)
    connect_db()
    wait_connection(socket)