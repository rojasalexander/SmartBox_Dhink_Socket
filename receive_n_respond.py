import socket
import time
from OpenBox import cajaNro

host = "192.168.40.41"
port = 5005

storedValue = "Sergio es Dios"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'EXIT':
            print("Our client has left us :(")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = 'Unknown Command'
            
        try: 
            if command == "BOX1":
                cajaNro(1)
                reply = "Abrimos caja 1"
            elif command == "BOX2":
                cajaNro(2)
                reply = "Abrimos caja 2"
            elif command == "BOX3":
                cajaNro(3)
                reply = "Abrimos caja 3"
            elif command == "BOX4":
                cajaNro(4)
                reply = "Abrimos caja 4"
        except:
            reply = "Error al abrir caja"

        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()
        

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break