import time
import socket
from datetime import datetime

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection From ",addr)
    a= str(datetime.now())
    client.send(a.encode())
    #client.send("\n",encode())
    time.sleep(2)
    disconnet_message = "\nYou are beging disconnected!\n"
    client.send(disconnet_message.encode())
    client.close()

