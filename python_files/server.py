import socket
import threading
from config import HEADER, PORT, FORMAT, DISCONNECT_MESSAGE

SERVER = socket.gethostbyname(
    socket.gethostname()
)
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection: {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    
    conn.close()

def start():
    server.listen()
    print(f"SERVER is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn,addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

start()