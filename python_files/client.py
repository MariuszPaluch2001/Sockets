import socket
from config import HEADER, PORT, FORMAT, DISCONNECT_MESSAGE

SERVER = socket.gethostbyname(
    socket.gethostname()
)
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def run():
    is_input = True
    while is_input:
        data = input("Type data. Type 'q' if you would like to exit.\n")
        if data == 'q':
            is_input = False
        else:
            send(data)
    
    send(DISCONNECT_MESSAGE)
    client.close()
    
    return 0

run()