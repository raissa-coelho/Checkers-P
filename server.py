import socket
from _thread import start_new_thread
import pickle
from game import Game

server = "127.0.0.1"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started.")


def thread_client(CONN):
    CONN.send(str.encode("Connected"))
    rep = ""
    while True:
        try:
            data = CONN.recv(2048)
            rep = data.decode("utf-8")

            if not data:
                print("Disconnected.")
                break
            else:
                print("Received: ", rep)
                print("Sending: ", rep)
            CONN.sendall(str.encode(rep))
        except:
            break
    print("Lost connection.")
    CONN.close()
    
while True:
    conn , addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(thread_client, (conn,))