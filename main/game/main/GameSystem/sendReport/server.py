import socket
import threading


PORT = 2411
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
OTHERS = []


def client_handle(conn, addr):
    print(f'[NEW CONNECTION] {addr} conneted')
    connected = True
    while connected:
        msg_length = conn.recv(2048).decode(FORMAT)
        if msg_length:
            try:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    OTHERS.remove(conn)
                print(f'[{addr}] {msg}')
            except ValueError as e:
                print(e)

    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Sever is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handle, args=(conn, addr))
        thread.start()
        OTHERS.append(conn)


print('[STARTING] server is starting....')
start()
