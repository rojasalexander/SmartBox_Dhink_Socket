import socket
from time import sleep

host = '192.168.40.41'
port = 5005

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendReceive(s, message):
    s.send(str.encode(message))
    reply = s.recv(1024)
    print("We have received a reply")
    print("Sending a closing message.")
    s.send(str.encode("EXIT"))
    s.close()
    reply = reply.decode('utf-8')
    return reply

s = setupSocket()

reply = sendReceive(s, 'BOX4')
print("resp: ", reply)