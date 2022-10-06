import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(
    socket.gethostname()
)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "CLOSING_CONNECTION"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection: {addr} connected.")
    connected = True
    while connected:
        msg_length = int(conn.recv(HEADER).decode(FORMAT))
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")
    
    conn.close()
    
def start():
    server.listen()
    while True:
        addr, conn = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn,addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

print("Server is running...")
start()